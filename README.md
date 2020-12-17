# DriveTest-Date-Checker
A year after getting my learner's permit, I decided I was finally ready to take a road test. However, due to COVID-19, DriveTest centers were booked for months. I really didn't want to wait 4 months for a 10-minute road test and I noticed that sometimes, the DriveTest center would show an opening for a road test in a few weeks or even days, not months. I wasn't exactly sure why (I suspected that people may have been cancelling their tests), but this got me excited. 

The problem was that the openings would only show for a few minutes and then they would go away (I assumed that they were getting booked by other people), and I don't have the time to check the website hundreds of times a day. So, I created a Python script using Selenium that will open Chrome, visit the DriveTest website, enter my login credentials (redacted from this repository for security reasons), and tell me if there are any available road test bookings in the next month.

**Note:** If you want to use this script yourself, it only works if you already have an account with DriveTest (you registered for a road test previously).

**Note 2:** The script currently only works for certain locations near the GTA (about 15 locations). I'll update this repository with more locations soon, but if you want to do it yourself, you'll need to add the XPath values for each location you want the program to go through to the ```locations``` list. You will also need to update the logic for displaying the location's name on line 73.

**Note 3:** I would usually include GIFs or screenshots of the script working for projects like these, but there is too much sensitive information on every page of the DriveTest website (past the login screen) and blurring out everything is just impractical.
