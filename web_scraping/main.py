from indeed import get_indeed_jobs
from stack_over_flow import get_stackOverFlow_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
stack_over_flow_jobs = get_stackOverFlow_jobs()

jobs = indeed_jobs + stack_over_flow_jobs
save_to_file(jobs)
