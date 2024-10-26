# logger.remove()
# logger.add(sys.stdout, level="INFO")

from old_data.framework import BaseTaskClient

if __name__ == '__main__':
    # client = BaseTaskClient("./assert/config/mumu12.yaml").run_from_task_json('tasks/orb.task.json')
    # client = BaseTaskClient("./assert/config/mumu12.yaml").run_from_task_json('tasks/rogue.task.json')
    # client = BaseTaskClient("./assert/config/mumu12.yaml").run_from_task_json('tasks/test.task.json')
    # client = BaseTaskClient("./assert/config/mumu12.yaml").run_from_task_json('tasks/test_repeated_orb.task.json')
    client = BaseTaskClient("old_data/assert/config/mumu12.yaml").run_from_task_json('tasks/enter_battle.task.json')