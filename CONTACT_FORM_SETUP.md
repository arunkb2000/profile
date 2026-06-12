# Contact Form Google Sheets Integration

Your profile now has a working contact form that collects visitor inquiries. To enable it to save data to a Google Sheet, follow these steps:

## Setup Instructions

### Step 1: Create a Google Sheet
1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet named "Contact Form Responses"
3. Add column headers in the first row:
   - A1: `Name`
   - B1: `Email`
   - C1: `Phone`
   - D1: `Message`
   - E1: `Timestamp`

### Step 2: Create a Google Apps Script
1. Open your Google Sheet
2. Go to **Extensions → Apps Script**
3. Replace all the code with this script:

```javascript
function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    // Append the data to the sheet
    sheet.appendRow([
      data.name,
      data.email,
      data.phone,
      data.message,
      data.timestamp
    ]);
    
    // Send confirmation email (optional)
    MailApp.sendEmail(
      data.email,
      "Thanks for reaching out! - Arun Kumar Bisariya",
      `Hi ${data.name},\n\nThank you for your message. I've received your inquiry and will get back to you soon.\n\nBest regards,\nArun Kumar Bisariya`
    );
    
    return ContentService.createTextOutput(JSON.stringify({status: 'success', message: 'Data saved'}))
      .setMimeType(ContentService.MimeType.JSON);
  } catch(error) {
    return ContentService.createTextOutput(JSON.stringify({status: 'error', message: error.toString()}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

### Step 3: Deploy as Web App
1. Click on **Deploy** button (top right)
2. Select **New deployment**
3. Choose **type: Web app**
4. Set these parameters:
   - Execute as: Your Google Account
   - Who has access: Anyone
5. Click **Deploy**
6. Copy the **Deployment URL** (looks like: `https://script.google.com/macros/d/YOUR_SCRIPT_ID/userweb/exec`)

### Step 4: Update Your Profile
1. Open `/workspaces/profile/index.html`
2. Find this line (around line 290):
   ```javascript
   const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/d/YOUR_SCRIPT_ID/userweb/exec';
   ```
3. Replace `YOUR_SCRIPT_ID` with your actual deployment URL from Step 3

### Step 5: Test the Form
1. Go to your profile page
2. Scroll to "Get In Touch" section
3. Fill out the contact form and submit
4. Check your Google Sheet - the data should appear!

## Features Included

- ✅ Form validation (Name, Email, and Message are required)
- ✅ Data saved to Google Sheet automatically
- ✅ Confirmation email sent to the visitor
- ✅ User-friendly success/error messages
- ✅ Timestamp recorded for each submission
- ✅ Mobile-responsive form

## Troubleshooting

**Form not submitting?**
- Check that you've updated the `GOOGLE_SCRIPT_URL` in index.html
- Ensure the Apps Script is deployed correctly
- Check browser console for errors (F12 → Console)

**Data not appearing in Sheet?**
- Verify the script is deployed as a Web App
- Check that "Who has access" is set to "Anyone"
- Ensure column headers are in row 1

**Confirmation emails not sending?**
- Google may require additional permissions on first run
- Click through the permission prompts in Apps Script

## Security Notes

- All data is saved only to your Google Sheet
- Emails are sent via Gmail (requires Gmail account)
- Consider adding CAPTCHA if you get spam submissions
- The endpoint is public but only accepts POST requests with the expected format

---

For help, contact: arun.dakshana17@gmail.com
