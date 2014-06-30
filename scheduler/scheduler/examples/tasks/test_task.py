"""
Test that tasks get executed properly using zookeeper
"""
from ds_commons.log import log
from ds_commons import argparse_tools as at


def main(textFile, ns, **job_id_identifiers):
    if ns.disable_log:
        import logging
        logging.disable = True
    log.info('test_module!!!')
    log.info('default ns: %s' % ns)
    if ns.fail:
        raise Exception("You asked me to fail, so here I am!")


build_arg_parser = at.build_arg_parser([at.group(
    "Test spark task",
    at.add_argument('--fail', action='store_true'),
    at.add_argument('--disable_log', action='store_true'),
    at.add_argument('--textFile', default=True),
    at.s3_key_bucket(type='read', default_key='fake_read_fp'),
)], conflict_handler='resolve'
)