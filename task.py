# based on the three experiments!/usr/bin/env python
# coding=utf-8

from aeneas.tools.execute_task import ExecuteTaskCLI

ExecuteTaskCLI(use_sys=False).run(arguments=[
    None,
    u"test_videos/test-trim-sox.mp3",
    u"test_file/test-trim1.txt",
    u"task_language=eng|is_text_type=plain|os_task_file_format=csv|task_adjust_boundary_nonspeech_min=0.010|task_adjust_boundary_nonspeech_string=REMOVE|task_adjust_boundary_algorithm=rateaggressive|task_adjust_boundary_rate_value=14.000",
    u"output/test-map2.csv"
])