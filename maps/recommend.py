"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################


def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    我应该创建一个字典，key是每一个centroid，value是它对应的距离。最后我要返回距离最小的value的key
    注意：字典的key必须是immutable value！所以不能直接用list！
    有一个问题是，如果multiple centroids are equally close，我怎么判断这一点？
    虽然现在写的code已经pass了，但是刚才好像没有考虑这个问题啊，是min()的性质就是这样的吗？
    """
    # BEGIN Question 3
    "*** YOUR CODE HERE ***"
    dic = {tuple(i): distance(i, location) for i in centroids}
    return list(min(dic, key = lambda ky: dic[ky]))
    # END Question 3


def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.
    额，绕绕，直接看例子就懂了，group together all values for the same key in a list of [key, value] pairs
    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    首先我要得到一个内涵每个餐厅location的列表，然后遍历其中的每一个location；
    看看对于某个location来说，它会选择哪个centroid（最近的那个）；
    然后，把选择了相同centriod的餐厅放在同一个list里面 →形成一个cluster
    不懂，为什么我的code不能pass，是哪里违反了abstraction barrier吗？？没有啊。
    啊，检查了半天，原来是最后它要return restaurant 而不是location啊。
    """
    # BEGIN Question 4
    "*** YOUR CODE HERE ***"
    all_c = [[find_closest(restaurant_location(r), centroids), r] for r in restaurants]
    return group_by_first(all_c)
    # END Question 4


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster.
    text中有说明，我们知道location是经纬度的list，所以用list索引不算是违背abstraction barrier噢。
    """
    # BEGIN Question 5
    "*** YOUR CODE HERE ***"
    #all_loc_lat = []
    #all_loc_lon = []
    #for i in cluster:
    #    lat = restaurant_location(i)[0]
    #    all_loc_lat += [lat]
    #    lon = restaurant_location(i)[1]
    #    all_loc_lon += [lon]
    all_loc_lat = [restaurant_location(i)[0] for i in cluster]
    all_loc_lon = [restaurant_location(i)[1] for i in cluster]
    avg_lat = mean(all_loc_lat)
    avg_lon = mean(all_loc_lon)
    return [avg_lat, avg_lon]



    # END Question 5


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        "*** YOUR CODE HERE ***"
        centroids = []
        for i in group_by_centroid(restaurants, old_centroids):
            centroids += [find_centroid(i)]
        # END Question 6
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    reviews_by_user = {review_restaurant_name(review): review_rating(review)
                       for review in user_reviews(user).values()}
    #review_restaurant_name()：Return the restaurant name of the review, which is a string
    #review_rating(): Return the number of stars given by the review, a floating point number between 1 and 5.
    #user_reviews():Return a dictionary from restaurant names to reviews by the user.
    xs = [feature_fn(r) for r in restaurants] # the extracted feature value for each restaurant in restaurants
    ys = [reviews_by_user[restaurant_name(r)] for r in restaurants] # user 对于在restaurants中的餐厅的评分

    # BEGIN Question 7
    #b, a, r_squared = 0, 0, 0  # REPLACE THIS LINE WITH YOUR SOLUTION
    mean_x, mean_y = mean(xs), mean(ys)
    Sxx = sum([(x - mean_x)**2 for x in xs])
    Syy = sum([(y - mean_y)**2 for y in ys])
    Sxy = sum([(x - mean_x) * (y - mean_y) for x, y in zip(xs, ys)]) # 别忘记把乘号*打出来啊！
    b = Sxy / Sxx
    a = mean_y - b * mean_x
    r_squared = Sxy ** 2 / (Sxx * Syy) # 套个括号能保证不出问题
    # END Question 7

    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    # user_reviewed_restaurants(): Return the subset of restaurants reviewed by user.
    # BEGIN Question 8
    "*** YOUR CODE HERE ***"
    predictor_and_r2 = [list(find_predictor(user, reviewed, feature_f)) for feature_f in feature_fns]
    max_one = max(predictor_and_r2, key=lambda ky: ky[1])
    return max_one[0]
    # END Question 8


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.
    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    # user_rating(): Return the rating given for restaurant_name by user.
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 9
    "*** YOUR CODE HERE ***"
    a = [{restaurant_name(res): user_rating(user, restaurant_name(res))} for res in reviewed]
    not_rated = [res for res in restaurants if res not in reviewed]
    b = [{restaurant_name(res): predictor(res)} for res in restaurants if res not in reviewed]
    #return a[0] + b[0] 啊，两个dict为什么不能相加啊.查了一下，A,B两个字典相加可以用 A.update(B),
    # 然后A是相加之后的大字典
    a[0].update(b[0])
    #return a[0]
    #--以上是最开始写的方法，或者也可以直接用for循环写？-----我是分割线哈-----
    # 下面写的也pass了 :)
    pre_list = []
    for res in restaurants:
        if res in reviewed:
            pre_list += [[restaurant_name(res), user_rating(user, restaurant_name(res))]]
        else:
            pre_list += [[restaurant_name(res), predictor(res)]]
    pre_dict = {pre[0]: pre[1] for pre in pre_list}
    return pre_dict
    # END Question 9


def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants 应该是a list of restaurants吧
    """
    # BEGIN Question 10
    "*** YOUR CODE HERE ***"
    # restaurant_categories():Return the categories of the restaurant, which is a list of strings.
    return [res for res in restaurants if query in restaurant_categories(res)]
    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)