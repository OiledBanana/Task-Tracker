import task
import sys
class Taskcli:
    def display_usage():
        print("Usage: task cli <command> [options]")
        print("commands:")
        print("add <description>                Add a new task")
        print("update <id> <new description>    Update a task")
        print("delete <id>                      Delete a task")
        print("mark-in-progress <id>            Mark task as in progress")
        print("mark-done <id>                   Mark task as done")
        print("list [status]                    List all task or filter by status")

    
    def handle_command(args):
        if len(args) < 2:
            Taskcli.display_usage()
            return
        command = args[1]

        if command == "add" and len(args) == 3:
            task.TaskManager.add_task(args[2])
        elif command == "update" and len (args) == 4:
            Taskcli._execute_with_id(args[2], lambda task_id: task.TaskManager.update_task(task_id, args[3]))
        elif command == "delete" and len (args) == 3:
            Taskcli._execute_with_id(args[2], lambda task_id: task.TaskManager.delete_task(task_id) )
        elif command == "mark-in-progress" and len(args) == 3:
            Taskcli._execute_with_id(args[2], lambda task_id: task.TaskManager.mark_task(task_id, "in-progress"))
        elif command == "mark-done" and len(args) == 3:
            Taskcli._execute_with_id(args[2], lambda task_id: task.TaskManager.mark_task(task_id,"done"))
        elif command == "list":
            status = args[2] if len(args) == 3 else None
            if status  in [None, "todo", "in-progress", "done"]:
                task.TaskManager.list_tasks(status)
            else:
                print("Invalid status. Use 'todo', 'in-progress', or 'done'. ")
        else:
            Taskcli.display_usage()

    def _execute_with_id(id_str, func):
        
        try:
            task_id =  int(id_str)
            func(task_id)
        except ValueError:
            print("Invalid task ID")

if __name__ == '__main__':
    Taskcli.handle_command(sys.argv)
        