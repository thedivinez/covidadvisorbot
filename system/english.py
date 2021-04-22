class English:
  NOT_AUTHORIZED_MESSAGE = "Sorry, You are not authorised to use this platform."
  RESTART_MESSAGE = "Restarting screaning process. Reply with <strong>Hi</strong> to continue."
  INVALID_INPUT_MESSAGE = "Invalid input reply with <strong>Yes</strong> or <strong>No</strong>."
  WELCOME_MESSAGE = "Please confirm you are 18 and above.<br>Reply with <strong>Yes</strong> to confirm or <strong>No</strong> to cancel."
  VIEW_OR_RESTART_MESSAGE = "Please reply with <strong>Yes</strong> to view screaning results or <strong>No</strong> to restart screaning."
  REJECT_MESSAGE = "Thank you for contacting us how ever you are not authorized to use this platform because of age. See you when you are old enough."
  LANGUAGE_MESSAGE = "Welcome to Covid Self Screaning please choose your language<br><br>Reply with <strong>EN</strong> for English or <strong>SH</strong> for Shona"

  symptoms = \
  """<strong>Are you experiencing any of these symptoms?</strong><br><br>
  
• Fever or feeling feverish (chills, sweating)<br>
• Difficulty breathing (not severe)<br>
• New or worsening cough<br>
• Sore throat<br>
• Whole body aches<br>
• Vomiting or diarrhea<br><br>

Reply with <strong>Yes</strong> or <strong>No</strong>"""

  exposures = """\
<strong>In the last 2 weeks, have you had any of the following exposures?</strong><br><br>

• Contact with a COVID-19+ person<br>
• International travel<br>
• Live in or have visited a place where COVID-19 is widespread<br><br>

Reply with <strong>Yes</strong> or <strong>No</strong>"""

  conditions = """\
<strong>Do you have any of the following conditions?</strong><br><br>
• Chronic lung disease or moderate to severe asthma<br>
• Congestive heart failure<br>
• Diabetes with complications<br>
• Neurologic conditions that weaken ability to cough<br>
• People with weakened immune systems<br>
• Dialysis<br>
• Cirrhosis of the liver<br>
• Pregnancy<br>
• Extreme obesity (BMI ≥ 40)<br><br>

Reply with <strong>Yes</strong> or <strong>No</strong>"""

  QUESTIONS = {
      0: {
          "column": "fullname",
          "question": "What is your full name?"
      },
      1: {
          "column": "dob",
          "question": "What's your date of birth?"
      },
      2: {
          "column": "symptoms",
          "question": symptoms
      },
      3: {
          "column": "exposures",
          "question": exposures
      },
      4: {
          "column": "conditions",
          "question": conditions
      },
      5:
      "Thank you for using our platform you you want to view results.<br><br> Reply with <strong>Yes</strong> to view or <strong>No</strong> to restart."
  }

  NO_TO_ALL_RESULTS = "Testing is not recommended at this time practice social distancing and wear a mask."
  SYMPTOMS_RESULTS = "Testing recommended please contact your health care provider if symptoms worsen and self isolate."
  ALL_CONDITIONS_RESULTS = "Testing is highly recommended condact your healthcare provider emmidiately and self isolate."
  CONDITIONS_NO_SYMPTOMS_RESULTS = "Testing is not recommended at this time practice social distancing obtain 30 day supply of medications."
  EXPOSURES_NO_SYMPTOMS_RESULTS = "Testing is not recommended at this time self isolate and contact your healthcare provider if you see any symptoms."
  UNIVERSAL_RESULTS = "Testing may be recommended please contact your health care provider if you have symptoms, self isolate and always wear your mask."