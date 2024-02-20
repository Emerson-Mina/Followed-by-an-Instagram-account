# Instagram Follower Tracker

**Python project to retrieve and compare Instagram account followers.**

---

## 🚨 Warning

**Please be aware that making too many requests to the Instagram API may result in your account being restricted or blocked. Use this project responsibly and do not exceed the recommended request limits by Instagram to avoid issues.**

---

## Introduction

This project aims to provide tools to retrieve and compare followers of an Instagram account using the Instagram private API. It consists of two main scripts:

- `follower.py`: A script to retrieve followers of an Instagram account and store them in a text file.
- `compare.py`: A script to compare previously retrieved followers with new followers and display the changes.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Emerson-Mina/Followed-by-an-Instagram-account.git
    ```

2. **Install Dependencies:**

    - Ensure you have Python 3.x installed on your system.
    - Install necessary dependencies using pip and the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Retrieving Followers

1. Open the `follower.py` file in a text editor.
2. Specify your Instagram account username in the `username` variable.
3. Specify the username of the Instagram account from which you want to retrieve followers in the `target_username` variable.
4. Specify the exact number of followers you want to retrieve in the `exact_followers_count` variable.
5. Run the `follower.py` script.

### Comparing Followers

1. Save the old followers in a file named `old_followers.txt` and the new followers in a file named `new_followers.txt`.
2. Run the `compare.py` script.
3. The script will display the followers removed and added between the old and new followers.

## Contribution

Contributions are welcome. If you wish to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution: `git checkout -b my_contribution`
3. Make your changes and ensure you follow coding style guidelines and best practices.
4. Commit your changes: `git commit -m "Add my contribution"`
5. Push your changes to your repository: `git push origin my_contribution`
6. Create a pull request on the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Author: [Emerson Mina](https://github.com/Emerson-Mina)
