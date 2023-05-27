#  Cafe Hunt Web App

This is a simple Flask web application that allows users to add and view cafes. Users can submit information about a cafe, including its name, location on Google Maps, opening and closing times, coffee rating, wifi strength rating, and power socket availability. The submitted data is stored in a CSV file and displayed on the website.

## Installation

To run this application on your local machine, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/MirelaManta/perfect-cafe-hunt
   ```

2. Change into the project directory:

   ```
   cd perfect-cafe-hunt
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set the `SECRET_KEY` environment variable. You can either set it directly in your system environment or create a `.env` file in the project directory and add the following line:

   ```
   SECRET_KEY=your-secret-key
   ```

5. Run the application:

   ```
   python main.py
   ```

6. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage

- Home Page: The home page provides a brief introduction to the cafe app. From here, you can navigate to the "Add a Cafe" page by entering http://localhost:5000/add in your browser's address bar.

- Add a Cafe: Fill out the form with the required information about the cafe and submit it. If the form inputs are valid, the cafe will be added to the list.

- View Cafes: By clicking the "Show Me" button from home page or by entering http://localhost:5000/cafes in the navigation bar, you can view the list of cafes. The cafes are displayed with their respective details, including name, location, opening and closing times, coffee rating, wifi strength rating, and power socket availability.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.
