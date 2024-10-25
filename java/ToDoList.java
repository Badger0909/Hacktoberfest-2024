import java.util.ArrayList;
import java.util.Scanner;

public class ToDoList {
    private ArrayList<String> tasks;

    public ToDoList() {
        tasks = new ArrayList<>();
    }

    // Method to add a task
    public void addTask(String task) {
        tasks.add(task);
        System.out.println("Task added: " + task);
    }

    // Method to remove a task
    public void removeTask(int index) {
        if (index >= 0 && index < tasks.size()) {
            String removedTask = tasks.remove(index);
            System.out.println("Task removed: " + removedTask);
        } else {
            System.out.println("Invalid task number.");
        }
    }

    // Method to display all tasks
    public void displayTasks() {
        if (tasks.isEmpty()) {
            System.out.println("No tasks in the list.");
            return;
        }
        System.out.println("To-Do List:");
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }

    public static void main(String[] args) {
        ToDoList toDoList = new ToDoList();
        Scanner scanner = new Scanner(System.in);
        String command;

        System.out.println("Welcome to the To-Do List Application!");

        do {
            System.out.println("\nCommands: add, remove, display, exit");
            System.out.print("Enter command: ");
            command = scanner.nextLine().toLowerCase();

            switch (command) {
                case "add":
                    System.out.print("Enter task description: ");
                    String task = scanner.nextLine();
                    toDoList.addTask(task);
                    break;
                case "remove":
                    System.out.print("Enter task number to remove: ");
                    int taskNumber = scanner.nextInt();
                    scanner.nextLine();  // Consume newline
                    toDoList.removeTask(taskNumber - 1); // Convert to 0-based index
                    break;
                case "display":
                    toDoList.displayTasks();
                    break;
                case "exit":
                    System.out.println("Exiting application.");
                    break;
                default:
                    System.out.println("Invalid command. Please try again.");
            }
        } while (!command.equals("exit"));

        scanner.close();
    }
}
