class Shona:
  RESTART_MESSAGE = "Tave kutangazve kuongorora."
  NOT_AUTHORIZED_MESSAGE = "Ndine urombo, Hauna mvumo yekushandisa chikuva ichi."
  INVALID_INPUT_MESSAGE = "Ndine hurmbo waisa mhinduro isiriyo, pindura ne <strong>Hongu</strong> kana <strong>Kwete</strong>"
  WELCOME_MESSAGE = "Ndokumbira usimbise kuti une makore 18 zvichienda mberi. Pindura uchiti <strong>Hongu</strong> kubvuma kana <strong>Kwete</strong> kuti ukukanzure"
  VIEW_OR_RESTART_MESSAGE = "Ndokumbirawo upindure uchiti <strong> Hongu </strong> kuti utarise zviongororwa kana <strong>Kwete</strong> kuti utangezve kuongorora."
  REJECT_MESSAGE = "Ndinokutendai nekutaura nesu asi tine hurombo kuti haubvumidzwe kushandisa chikuva ichi nekuda kwezera. Toonana kana wakura zvakakwana."
  LANGUAGE_MESSAGE = "Tinokugamuchirai kuCovid Self Screaning ndapota sarudza mutauro wako <br> Pindura uchiti <strong>EN</strong> kana uchida chirungu kana <strong>SH</strong> kana uchida shona."

  symptoms = \
  """<strong> Uri kusangana nechimwe chezviratidzo izvi? </strong> <br> <br>
  
• Fivha kana kunzwa kupisa (kutonhora, kudikitira) <br>
• Kunetseka kufema (kwete kwakanyanya) <br>
• Kukosora kutsva kana kudzikira <br>
• Huro pahuro <br>
• Kurwadziwa kwemuviri wese <br>
• Kurutsa kana kuita manyoka <br> <br>

Pindura uchiti <strong>Hongu</strong> kana <strong> Kwete </strong>"""

  exposures = """\
<strong> Mumavhiki maviri apfuura, wakambove nekumwe kufumurwa kunotevera?</strong><br><br>

• Bata neCOVID-19 + munhu <br>
• Kufamba kwenyika dzese <br>
• Gara mukati kana kushanyira nzvimbo ine COVID-19 yakapararira <br> <br>

Pindura ne <strong>Hongu</strong> kana <strong>Kwete</strong>"""

  conditions = """\
<strong>Iwe une chero cheanotevera mamiriro?</strong><br><br>

• Chirwere chemapapu chisingaperi kana chipfuva chakadzikira kusvika chakakomba<br>
• Kugumbuka kwemoyo kukundikana<br>
• Chirwere cheshuga chine matambudziko<br>
• Neurologic mamiriro ayo anoderedza kugona kukosora<br>
• Vanhu vane immune system isina kusimba <br>
• Dialysis <br>
• Cirrhosis yechiropa <br>
• Kubata Pamuviri
• Kunyanyisa kufutisa (BMI ≥ 40) <br> <br>

Pindura uchit <strong>Hongu</strong> kana <strong>Kwete</strong>"""

  QUESTIONS = {
      0: {
          "column": "fullname",
          "question": "Zita rako rizere ndiani?"
      },
      1: {
          "column": "dob",
          "question": "Ndeupi wako musi wekuzvarwa?"
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
      "Ndatenda nekushandisa chikuva chedu iwe unoda kuona mhedzisiro here. <br><br>Pindura uchiti <strong>Hongu</strong> kuona kana <strong>Kwete</strong> kutangazve."
  }

  NO_TO_ALL_RESULTS = "Kuvhenekwa nachiremba kakusi kukurudzirwa panguva ino chimbozvisudurutsa pane vanhu uye pfeka mask."
  ALL_CONDITIONS_RESULTS = "Kuedzwa nachiremba kunokurudzirwa zvikuru ita kuti mupi wako wezvehutano akuone nekuchimbidza uye zviparadzanise nevanhu."
  SYMPTOMS_RESULTS = "Kuvhenekwa nachiremba kunokurudzirwa ndapota nyorera mupi wako wezvehutano kana zviratidzo zvanyanya uye zviparadzanise nevanhu."
  CONDITIONS_NO_SYMPTOMS_RESULTS = "Kuvhenekwa nachiremba hakukurudzirwi panguva ino kudzidzira zviparadzanise nevanhu uye wana mishonga inokwana mazuva makumi matatu."
  EXPOSURES_NO_SYMPTOMS_RESULTS = "Kuvhenekwa nachiremba hakuna kukurudzirwa panguva ino kuzviparadzanisa wega uye bata mupi wako wezvehutano kana ukaona chero zviratidzo zveCovid."
  UNIVERSAL_RESULTS = "Kuvhenekwa nachiremba kunogona kukurudzirwa ndapota nyorera wako mupi wezvehutano kana iwe uine zviratidzo, kuzviparadzanisa uye kugara uchipfeka mask yako."