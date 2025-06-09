# LitList
A web application built with Vue + Vite frontend and Flask backend. 

LitList is a simple book tracking app that lets you keep a record of books you've read, and those you haven't finished yet. It's a personal reading progress tracker.

## Features
- Create, read, update, delete, and list (CRUDL) operations for books
- Data storage using SQLite
- Utilizes pagination for data display
- Search and sort operations
- Light/dark mode support

## To run the project locally

### Clone the respository
```bash
git clone https://github.com/xbryan25/litlist.git
cd litlist
```
### Backend Setup
1. Navigate to the backend directory
   
    ```bash
    cd backend
    ```

2. Create and activate a virtual environment
   
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    python -m venv venv
    source venv/Scripts/activate
    ```

3. Once in the virtual environment, install dependencies
   
    ```bash
    pip install -r requirements.txt
    ```

4. Switch to the working directory

    ```bash
    cd src
    ```

5. Start the Flask application

    ```bash
    python run.py
    ```

6. To stop the Flask application, press CTRL + C in the terminal to quit

7. To deactivate the virtual environment

    ```bash
    deactivate
    ```

### Frontend Setup
1. Navigate to the backend directory
   
    ```bash
    cd frontend
    ```

2. Install the required Node packages
   
    ```bash
    npm install
    ```

3. Start the Vue application

    ```bash
    npm run start
    ```

4. To stop the Vue application, press CTRL + C and type 'y' in the terminal to quit

## Technology Stack

- **Frontend**: Vue, Vite, TailwindCSS
- **Backend**: Flask
- **Database**: SQLite

## Feedback

If you have any feedback, please reach out to @xbryan25 using this [email](mailto:bryanaganp25@gmail.com)

## License
This project is licensed under the MIT License.