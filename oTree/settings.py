from os import environ
import os

SESSION_CONFIGS = [

#    dict(
    #          name='Video1',
    #   app_sequence=['video'],
    #   num_demo_participants=100,
    #   cc_code="CCCODE",
    #   error_code="ECODE",
    #   ),
    #  dict(
    #   name='Video2',
    #   app_sequence=['video2'],
    #   num_demo_participants=100,
    #   cc_code="CCCODE",
    #   error_code="ECODE",
    #  ),
    #  dict(
    #      name='Video3',
    #   app_sequence=['video3'],
    #   num_demo_participants=100,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
    #  dict(
    #      name='Video4',
    #      app_sequence=['video4'],
    #      num_demo_participants=100,
    #      cc_code="CCCODE",
#      error_code="ECODE",
    #   ),
#  dict(
    #       name='menus_evideo',
    #   app_sequence=['menus_evideo'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #    ),
#  dict(
    #       name='SimpleRanking_ties',
    #   app_sequence=['RET','RankingSimple'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#  dict(
    #       name='RankingSimple_ties_grass',
    #   app_sequence=['RET','RankingSimple_grass'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#  dict(
    #       name='SimpleRanking_Incentives1',
    #   app_sequence=['RankingSimple_Incentives1'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #    ),
#  dict(
    #       name='SimpleRanking_TiesIncentives',
    #   app_sequence=['RankingSimple_tiesincentives'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#  dict(
    #       name='NoRanking',
    #   app_sequence=['RET','NoRanking'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#    dict(
    #    name='NoRanking_grass',
    #       app_sequence=['RET','NoRanking_grass'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#  dict(
    #       name='BeforeAfter',
    #   app_sequence=['RET','BeforeAfter'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#  dict(
    #       name='BeforeAfter_ask',
    #   app_sequence=['RET','BeforeAfter_grass'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),
#  dict(
    #       name='BeforeAfter_SKIP2',
    #   app_sequence=['RET','BeforeAfter_Skip2'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #    ),
#  dict(
    #       name='BeforeAfter_SKIP_SP',
    #   app_sequence=['RET','BeforeAfter_Skip_SocialPressure'],
    #   num_demo_participants=2,
    #   cc_code="CCCODE",
#   error_code="ECODE",
    #   ),

#dict(
 #       name='VideoChoice',
  #      app_sequence=['RET','VideoChoice_Control','VideoChoice_Emotional',
   #                   'VideoChoice_PressureNoJ','VideoChoice_PressureJ'],
    #    num_demo_participants=2,
    #    cc_code="CCCODE",
#    error_code="ECODE",
    #),
#dict(
    #       name='VideoChoice_Emotional',
    #       app_sequence=['VideoChoice_Emotional'],
    #       num_demo_participants=2,
    #       cc_code="CCCODE",
#       error_code="ECODE",
    #   ),
#dict(
    #       name='VideoChoice_PressureNoJ',
    #       app_sequence=['VideoChoice_PressureNoJ'],
    #      num_demo_participants=2,
    #      cc_code="CCCODE",
#      error_code="ECODE",
    #  ),
#dict(
    #       name='VideoChoice_PressureJ',
    #       app_sequence=['VideoChoice_PressureJ'],
    #       num_demo_participants=2,
    #       cc_code="CCCODE",
#       error_code="ECODE",
    #   ),
#dict(
    #       name='VideoControl',
    #       app_sequence=['VideoChoice_Control'],
    #      num_demo_participants=2,
    #      cc_code="CCCODE",
#     error_code="ECODE",
    # )
dict(
          name='Survey_',
           app_sequence=['survey_'],
          num_demo_participants=2,
          cc_code="CCCODE",
     error_code="ECODE",
     ),
dict(
          name= 'DWK',
           app_sequence=['Welcome','DWK_baseline', 'DWK_cheap', 'DWK_increasedloss', 'DWK_likelyloss'],
          num_demo_participants=2,
          cc_code="CCCODE",
     error_code="ECODE",
     ),
dict(
          name= 'CWsurvey',
          app_sequence=['CWsurvey'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE",
     ),

dict(
          name= 'Video',
          app_sequence=['video_gemma'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE",
     ),
dict(
          name= 'Website',
          app_sequence=['website'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE",
     ),
dict(
          name= 'CWsurvey2',
          app_sequence=['CWsurvey2'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),
dict(
          name= 'CWsurvey2_netquest1',
          app_sequence=['CWsurvey_netquest1'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),
dict(
          name= 'CWsurvey2_netquest2',
          app_sequence=['CWsurvey_netquest2'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),
dict(
          name= 'CWsurvey2_netquest3',
          app_sequence=['CWsurvey_netquest3'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),
dict(
          name= 'CWsurvey2_netquest4',
          app_sequence=['CWsurvey_netquest4'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),
dict(
          name= 'CWsurvey2_netquest5',
          app_sequence=['CWsurvey_netquest5'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),
dict(
          name= 'CWsurvey2_netquest6',
          app_sequence=['CWsurvey_netquest6'],
          num_demo_participants=2,
          cc_code="CCCODE",
          error_code="ECODE"
     ),

]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


PARTICIPANT_FIELDS = ['number','is_dropout']

SESSION_FIELDS = ['params']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '{{ secret_key }}'
# RECAPTCHA V2
#RECAPTCHA_SITE_KEY = "6LfTTd8qAAAAAHEL6N4QHxAfE0-pW29Lwdm9DZzK"

#RECAPTCHA_SECRET_KEY = "6LfTTd8qAAAAAA_ECYNkXJd5_UCzp_Zx5pUs4TrW"


RECAPTCHA_SITE_KEY = os.getenv('RECAPTCHA_SITE_KEY')
RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')
REDIS_URL = os.getenv('REDISCLOUD_URL')

CHANNEL_ROUTING = {
    'backend': 'channels_redis.core.RedisChannelLayer',
    'config': {
        "hosts": [REDIS_URL],
    },
}
INSTALLED_APPS = ['otree']

DEBUG = False
