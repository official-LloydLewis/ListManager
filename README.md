---

# **ListManager Project**

## **Overview**

The ListManager Project is a comprehensive suite designed to manage and manipulate user data efficiently. This repository includes functionalities for managing user information, configuring settings, and displaying data through a customizable terminal application. The project is structured to provide a modular and extendable approach to user management.

### **Project Structure**

```
MANAGERS
├── Database
│   └── USERS.json
├── LM
│   ├── Config
│   │   └── config.yml
│   ├── ListManager
│   │   ├── add.py
│   │   ├── ConfigLoader.py
│   │   ├── remove.py
│   │   ├── show_list.py
│   │   └── USERS.py
│   └── ListManager-Plugin
├── .gitattributes
├── LICENSE
├── README.md
├── Main.py
└── ListManager.py
```

## **Features**

- **User Management**: Add, remove, and list users with customizable display options.
- **Configuration Management**: Load and manage application settings through a YAML configuration file.
- **Customizable Display**: Toggle the visibility of user data fields.
- **Modular Design**: Separate concerns with distinct modules for configuration loading, user management, and user data display.

## **Configuration**

The application configuration is managed through a YAML file located at `LM/Config/config.yml`. This file defines various settings and paths used by the application.

### **How It Works**

1. **Configuration Loading**: The `ConfigLoader.py` file reads the `config.yml` file and provides access to configuration settings. The configuration file path is dynamically determined relative to the script’s location, ensuring compatibility across different systems.
   
2. **Usage**:
   - **Configuration File**: Place the YAML configuration file in `LM/Config/config.yml`. Adjust paths and settings as needed.
   - **Running the Application**: Execute `Main.py` to start the application. It initializes the user management system and displays the interface based on the loaded configuration.
   - **Commands and Shortcuts**: Refer to the user interface for available commands and shortcuts for managing user data and configuring display options.

## **Usage**

### **Running the Application**

1. Clone the repository:

   ```sh
   git clone https://github.com/official-LloydLewis/ListManager
   ```

2. Navigate to the project directory:

   ```sh
   cd Managers/LM
   ```

3. Run the main application script:

   ```sh
   python Main.py
   ```

### **Configuration**

- Edit `LM/Config/config.yml` to update settings and paths as required. Ensure that the YAML structure is maintained for correct parsing.

### **User Management**

- Use the terminal interface to manage users. Commands and shortcuts for adding, removing, and listing users are provided within the application interface.

## **To Do List**

- **Add Sorting System**: Implement sorting functionality for user lists based on different criteria.
- **Add Search and Filter**: Introduce search and filter capabilities to make user data management more efficient.
- **Code Improvement**: Refactor and improve the existing codebase for better performance and readability.

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to adjust or expand any sections as needed!
