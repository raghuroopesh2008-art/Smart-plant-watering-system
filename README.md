# Smart Plant Watering Assistant

A simple website that follows the flowchart:

1. Enter plant name and soil moisture
2. Analyse the moisture percentage
3. Below 30 % (Dry): water the plant
4. 30 to 59 % (Moderate): give little water
5. 60 to 100 % (Wet): no watering
6. Show the final report and recommendation

The whole site is one file, `index.html`. No installation is needed to run it.

---

## Part 1: Run it on your computer

### Option A (easiest)
1. Open the `smart-plant-watering` folder.
2. Double-click `index.html`. It opens in your browser.

### Option B (local live server)
This runs the site at an address like `http://localhost:8000`.

1. Install Python from https://www.python.org/downloads/ if you do not have it.
2. Open a terminal inside the `smart-plant-watering` folder:
   - Windows: click the address bar of the folder, type `cmd`, press Enter.
   - Mac: right-click the folder and choose "New Terminal at Folder", or use Terminal.
3. Type this and press Enter:
   ```
   python -m http.server 8000
   ```
4. Open your browser and go to `http://localhost:8000`.
5. To stop the server, press `Ctrl + C` in the terminal.

### Option C (VS Code Live Server)
1. Install Visual Studio Code from https://code.visualstudio.com/
2. Open the folder in VS Code (File > Open Folder).
3. Install the extension "Live Server" by Ritwick Dey.
4. Right-click `index.html` and choose "Open with Live Server".
   The page reloads automatically when you save changes.

---

## Part 2: Upload to GitHub

### Step 1: Create a GitHub account
Go to https://github.com and sign up if you do not have an account.

### Step 2: Create a repository
1. Click the **+** icon at the top right and choose **New repository**.
2. Name it `smart-plant-watering`.
3. Keep it **Public**.
4. Do **not** tick "Add a README" (this folder already has one).
5. Click **Create repository**.

### Step 3: Upload the files
1. On the new repository page, click **uploading an existing file**.
2. Drag `index.html` and `README.md` into the box.
3. Click **Commit changes**.

### Step 4 (optional): Put the site online with GitHub Pages
1. In your repository, go to **Settings > Pages**.
2. Under "Branch", select `main` and `/ (root)`, then click **Save**.
3. After a minute, your site is live at
   `https://YOUR-USERNAME.github.io/smart-plant-watering/`.

---

## Notes
- The moisture input must be a whole number from 0 to 100.
- The page uses Google Fonts for typography. If you are offline, it still works with a standard font.
- Nothing is saved. Each check starts fresh.
