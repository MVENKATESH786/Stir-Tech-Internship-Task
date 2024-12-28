# Stir Tech Internship Task

## About the Project
This repository contains the solution for the Stir Tech Internship assignment. The task demonstrates skills in web scraping, proxy management, database integration, and creating a user-friendly interface to display the results.

### Features
1. **Web Scraping with Selenium**:
   - Automates login to Twitter to fetch the top 5 trending topics from the "What’s Happening" section.
   - Uses Selenium for browser automation.

2. **Proxy Management**:
   - Implements ProxyMesh to send requests from different IP addresses for each scrape.

3. **Database Integration**:
   - Stores scraped data in MongoDB with a unique ID, trends, timestamp, and IP address used.

4. **Interactive Webpage**:
   - A simple HTML page with a button to trigger the scraping script.
   - Displays the scraped trending topics, timestamp, and IP address.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Expected Output](#expected-output)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

---

## Technologies Used
- **Python**: Core programming language.
- **Selenium**: For web automation and scraping.
- **ProxyMesh**: For proxy rotation.
- **MongoDB**: NoSQL database to store scraped data.
- **Flask**: Framework to create the interactive webpage.

---

## Setup and Installation

### Prerequisites
1. Install Python (version 3.8 or higher).
2. Install MongoDB and ensure it’s running.
3. Install Chrome and [ChromeDriver](https://chromedriver.chromium.org/downloads) for Selenium.
4. Create a ProxyMesh account and get your proxy credentials.
5. Have a Twitter account ready for login.

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/MVENKATESH786/Stir-Tech-Internship-Task.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd Stir-Tech-Internship-Task
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Update the `config.py` file with your credentials:
   - Twitter username and password.
   - ProxyMesh credentials.
   - MongoDB connection string.

---

## How to Run

### Run Locally
1. Start MongoDB:
   ```bash
   mongod
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

4. Click the button on the webpage to trigger the scraping script.

### Note
Ensure that Twitter credentials are correct and ProxyMesh is properly configured.

---

## Expected Output
1. When the button is clicked, the page displays:
   - Top 5 trending topics.
   - Timestamp of the scrape.
   - IP address used for the request.
2. The data is also stored in MongoDB with the following structure:
   ```json
   {
       "_id": "unique_id",
       "trend1": "First Trending Topic",
       "trend2": "Second Trending Topic",
       "trend3": "Third Trending Topic",
       "trend4": "Fourth Trending Topic",
       "trend5": "Fifth Trending Topic",
       "datetime": "YYYY-MM-DD HH:MM:SS",
       "ip": "XXX.XXX.XXX.XXX"
   }
   ```

---

## Future Improvements
- Add error handling for login failures and scraping issues.
- Improve UI for better user experience.
- Support additional social media platforms.

---

## Acknowledgments
- **Stir Tech** for the internship opportunity.
- **Internshala** for hosting the program.
- Community contributors for Selenium and Flask documentation.

---

