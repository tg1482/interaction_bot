from instapy import InstaPy
from instapy.util import smart_run

# Write your automation here
# Stuck? Look at the github page https://github.com/InstaPy/instapy-quickstart

insta_username = ""
insta_password = ""

BIG_ACCOUNTS = ['fabcurate', 'picchika', 'shalvifashions', 'twinkle_collection_2020', 'azafashions', 'chandni_handloom']

ENTREPRENEUR_TAGS = ['selfmade', 
				'womanentrepreneur', 
                'womanownedbusiness', 
                'womeninbusiness',
				'smallbusinessowner',
                'smallbusiness',
				'giftshop', 
                'independentartist']


PRODUCT_TAGS = ['handmade',
                'handcrafted',
                'shopsmall',
                'shophandmade',
                'supporthandmade',
                'supportindiandesigners',
                'zerowaste',
                'sustainableliving',
                'sustainablelifestyle',
                'shopauthentic',
                'authentic',
                'unique',
                'decorlovers',
                'homedecor']


INDIAN_ETHNIC_TAGS =['indianart', 
                    'ethnic',
                    'indiandecor',
                    'heritage',
                    'authenticindian',
                    'madeinindia',
                    'makeinindia']


BLOCK_PRINTING_TAGS = ['blockprinting',
                        'blockprintedfabric',
                        'blockprintedsaree']


GIFT_TAGS = ['giftsforher',
            'giftsforhim',
            'holidaygift',
            'holiday',
            'handmadegifts',
            'sustainablegifts',
            'customgift',
            'custommade',
            'uniquegifts']

    
ALL_TAGS = ENTREPRENEUR_TAGS + PRODUCT_TAGS + INDIAN_ETHNIC_TAGS + BLOCK_PRINTING_TAGS + GIFT_TAGS

COMMENT_LIST = ['Beautiful :heart_eyes:',
                'Absolutely stunning :heart_eyes: :heart:',
                'Inspiring!']

session = InstaPy(username=insta_username,
                    password=insta_password,
                    headless_browser=True,
                    disable_image_load=True,
                    multi_logs=False,
                    # geckodriver_path="/assets/gecko/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz",
                    )


with smart_run(session):
    """
    Session Quota
    """
    session.set_quota_supervisor(enabled=True,
                                sleep_after=["likes", "follows"],
                                sleepyhead=True, stochastic_flow=True,
                                notify_me=True,
                                peak_likes_hourly=200,
                                peak_likes_daily=585,
                                peak_comments_hourly=80,
                                peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                peak_unfollows_hourly=35,
                                peak_unfollows_daily=402,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=4700)


    """
    Setting smooth behavior
    """
    session.set_simulation(enabled=True,
                       percentage=66)
    session.set_action_delays(enabled=True,
                          like=10,
                          comment=5,
                          follow=4.17,
                          unfollow=28)


    """
    Filters
    """
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=None, min_comments=10)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=None,
                                    max_following=5000,
                                    min_followers=50,
                                    min_following=50)

    """
    Interaction settings
    """
    session.set_do_follow(enabled=True, percentage=80, times=1)
    session.set_do_comment(enabled=True, percentage=5)
    session.set_comments(COMMENT_LIST,
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_user_interact(amount=5, randomize=True, percentage=80, media='Photo')

    # activity
    session.like_by_tags(ALL_TAGS, amount=80)
    session.follow_by_tags(ALL_TAGS, amount=80)
    session.follow_user_followers(BIG_ACCOUNTS, amount=800,
                                  randomize=False, interact=False)
    session.follow_user_following(BIG_ACCOUNTS, amount=10, randomize=False, sleep_delay=60)
    session.follow_likers(BIG_ACCOUNTS, photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
    session.follow_commenters(BIG_ACCOUNTS, amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=True)

    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=2 * 24 * 60 * 60, sleep_delay=501)

    session.unfollow_users(amount=100, nonFollowers=True, style="RANDOM", unfollow_after= 2 * 24 * 60 * 60, sleep_delay=655)
    session.end()


    # """ Joining Engagement Pods...
    # """
    # session.join_pods(topic='sports', engagement_mode='no_comments')
