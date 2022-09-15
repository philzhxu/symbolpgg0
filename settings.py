from os import environ

SESSION_CONFIGS = [
    dict(
       name='Dickson_Salary_full',
       display_name="Dickson_Salary_full",
       num_demo_participants=5,
       app_sequence=[
           'rule_base',
           'round_base',
           'survey',
       ]
    ),
    dict(
        name='Dickson_Salary_limited',
        display_name="Dickson_Salary_limited",
        num_demo_participants=5,
        app_sequence=[
            'rule_base_limited',
            'round_base_limited',
            'survey',
        ]
    ),
    dict(
        name='Dickson_Appropriation_full',
        display_name="Dickson_Appropriation_full",
        num_demo_participants=5,
        app_sequence=[
            'rule_appropriation_full',
            'round_appropriation_full',
            'survey',
        ]
    ),
    dict(
        name='Dickson_Appropriation_limited',
        display_name="Dickson_Appropriation_limited",
        num_demo_participants=5,
        app_sequence=[
            'rule_appropriation_limited',
            'round_appropriation_limited',
            'survey',
        ]
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True

ROOMS = [
    dict(
        name='salary_full',
        display_name='salary_full',
        participant_label_file='_rooms/participant.txt',
        use_secure_urls=True
    ),
    dict(
        name='salary_limited',
        display_name='salary_limited',
        participant_label_file='_rooms/participant.txt',
        use_secure_urls=True
    ),
    dict(
        name='appropriation_full',
        display_name='appropriation_full',
        participant_label_file='_rooms/participant.txt',
        use_secure_urls=True
    ),
    dict(
        name='appropriation_limited',
        display_name='appropriation_limited',
        participant_label_file='_rooms/participant.txt',
        use_secure_urls=True
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9%a@&i6ul7vowt9)z4ygpx&rtzjgy#e#-zs0&xe9o)%p(ch12#'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']



