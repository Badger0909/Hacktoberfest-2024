import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TextAdventureGame {
    private static Map<String, String> inventory = new HashMap<>();
    private static String currentLocation = "forest";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to the Text Adventure Game!");
        System.out.println("You find yourself in a dark forest. What do you want to do?");
        displayOptions();

        while (true) {
            System.out.print("> ");
            String input = scanner.nextLine().toLowerCase().trim();

            if (input.equals("quit")) {
                System.out.println("Thanks for playing! Goodbye!");
                break;
            } else if (input.equals("look") || input.equals("1")) {
                lookAround();
            } else if (input.startsWith("take ") || input.equals("2")) {
                handleTakeCommand(input);
            } else if (input.equals("inventory") || input.equals("3")) {
                showInventory();
            } else if (input.equals("go castle") || input.equals("4")) {
                currentLocation = "castle";
                System.out.println("You walk towards the castle.");
            } else if (input.equals("go village") || input.equals("5")) {
                currentLocation = "village";
                System.out.println("You walk towards the village.");
            } else if (input.equals("options") || input.equals("6")) {
                displayOptions();
            } else {
                System.out.println("I don't understand that command. Type 'options' for help.");
            }
        }
        scanner.close();
    }

    private static void displayOptions() {
        System.out.println("\nAvailable commands:");
        System.out.println("1. look - Look around your current location.");
        System.out.println("2. take [item] - Take an item from your surroundings.");
        System.out.println("3. inventory - Check your collected items.");
        System.out.println("4. go castle - Move to the castle.");
        System.out.println("5. go village - Move to the village.");
        System.out.println("6. options - Display this list of commands.");
        System.out.println("7. quit - Exit the game.\n");
    }

    private static void lookAround() {
        switch (currentLocation) {
            case "forest":
                System.out.println("You see tall trees surrounding you, and you can hear the distant sound of a river flowing.");
                break;
            case "castle":
                System.out.println("The castle looms above you, its gates are closed and guarded by a fierce-looking knight.");
                break;
            case "village":
                System.out.println("You see villagers going about their day, trading goods and chatting with each other.");
                break;
            default:
                System.out.println("You are lost in an unknown place.");
        }
    }

    private static void handleTakeCommand(String input) {
        if (input.equals("2")) {
            System.out.println("Please specify an item to take (e.g., 'take sword').");
            return;
        }

        String item = input.substring(5).trim(); // Extract item name
        switch (currentLocation) {
            case "castle":
                if ("sword".equalsIgnoreCase(item)) {
                    inventory.put(item, "A shiny sword, perfect for battles.");
                    System.out.println("You have taken the sword!");
                } else {
                    System.out.println("There is no such item here in the castle.");
                }
                break;
            case "village":
                if ("potion".equalsIgnoreCase(item)) {
                    inventory.put(item, "A healing potion that restores health.");
                    System.out.println("You have taken the potion!");
                } else {
                    System.out.println("There is no such item here in the village.");
                }
                break;
            default:
                System.out.println("You cannot take items from here.");
        }
    }

    private static void showInventory() {
        if (inventory.isEmpty()) {
            System.out.println("\nYour inventory is empty.\n");
        } else {
            System.out.println("\nYou have:");
            for (String item : inventory.keySet()) {
                System.out.printf("- %s: %s%n", item, inventory.get(item));
            }
            System.out.println();
        }
    }
}
