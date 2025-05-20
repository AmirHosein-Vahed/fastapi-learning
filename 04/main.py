#------------------------------------------------------
#
#               ENVIRONMENT VARIABLES
# 
# https://fastapi.tiangolo.com/environment-variables/
# 
#------------------------------------------------------

import os

user = os.getenv("USER", "AmirHosein")
print(user)

#------------------------------------------------------
#
#               VIRTUAL ENVIRONMENTS
# 
# https://fastapi.tiangolo.com/virtual-environments/
# 
#------------------------------------------------------

# uv venv
# python -m venv .venv
# virtualenv .venv .