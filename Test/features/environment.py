from httpx import get
from behave import *
def before_all(context):
 context.url = context.config.userdata.get('url')
