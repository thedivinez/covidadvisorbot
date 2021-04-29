from system.shona import Shona as sh
from system.english import English as en
from system.config import table, db_query


class CovidScreaning:
  def getdata():
    return table.table("subjects").all()

  def language(ip_address: str):
    return sh if CovidScreaning.user_data_in_db(ip_address).get("language") == "sh" else en

  def translate(message: str):
    if message.lower() == "hongu":
      message = "yes"
    elif message.lower() == "kwete":
      message = "no"
    return message

  def listen(request: dict) -> str:
    ip_address = str(request["ip_address"])
    message = CovidScreaning.translate(request["message"])
    user = CovidScreaning.user_data_in_db(ip_address)  # grab user data
    if not user:
      if message.lower() in ["en", "sh"]:
        userdata = {"ip_address": ip_address, "language": message}
        question = en.WELCOME_MESSAGE if message.lower() == "en" else sh.WELCOME_MESSAGE
        return CovidScreaning.update_user_data(userdata, question)
      return en.LANGUAGE_MESSAGE
    else:
      ln = CovidScreaning.language(ip_address)  # choose language
      if not "stage" in user.keys():
        userdata = {"ip_address": ip_address, "authorised": message, "stage": 0}
        if message.lower() == "yes":
          return CovidScreaning.update_user_data(userdata, ln.QUESTIONS[0]["question"])
        elif message.lower() == "no":
          return ln.REJECT_MESSAGE
        return ln.WELCOME_MESSAGE
      else:
        if user.get("authorised").lower() == "yes":
          stage = int(user.get("stage") + 1)
          if stage - 1 in [3, 4, 5] and not message.lower() in ["yes", "no"]:
            return ln.INVALID_INPUT_MESSAGE
          if stage in ln.QUESTIONS.keys():
            column = ln.QUESTIONS[stage - 1]["column"]
            userdata = {"stage": stage, "ip_address": ip_address, column: message}
            question = ln.QUESTIONS[stage] if stage == max(ln.QUESTIONS.keys()) else ln.QUESTIONS[stage]["question"]
            return CovidScreaning.update_user_data(userdata, question)
        else:
          return ln.NOT_AUTHORIZED_MESSAGE
        return CovidScreaning.finalise_screaning(ln, message, ip_address)

  def user_data_in_db(ip_address: str):
    user = table.table("subjects").get(db_query.ip_address == ip_address)
    return user if user else {}

  def current_stage(ip_address: str) -> str:
    return CovidScreaning.user_data_in_db(ip_address).get("stage")

  def update_user_data(userdata: dict, result: str):
    user = CovidScreaning.user_data_in_db(userdata["ip_address"])
    if user:
      table.table("subjects").update(userdata, db_query.ip_address == userdata["ip_address"])
    else:
      table.table("subjects").insert(userdata)
    return result

  def restartscreaning(language, ip_address: str) -> str:
    table.remove(db_query.ip_address == ip_address)
    return language.RESTART_MESSAGE

  def generate_screaning_results(lang, ip_address: str) -> str:
    user = CovidScreaning.user_data_in_db(ip_address)
    if user["symptoms"] == "yes" and user["exposures"] == "yes" and user["conditions"] == "yes":
      return lang.ALL_CONDITIONS_RESULTS
    if user["symptoms"] == "yes" and user["exposures"] == "no" and user["conditions"] == "no":
      return lang.SYMPTOMS_RESULTS
    if user["symptoms"] == "no" and user["exposures"] == "yes" and user["conditions"] == "no":
      return lang.EXPOSURES_NO_SYMPTOMS_RESULTS
    if user["symptoms"] == "no" and user["exposures"] == "no" and user["conditions"] == "yes":
      return lang.CONDITIONS_NO_SYMPTOMS_RESULTS
    if user["symptoms"] == "no" and user["exposures"] == "no" and user["conditions"] == "no":
      return lang.NO_TO_ALL_RESULTS
    return lang.UNIVERSAL_RESULTS

  def finalise_screaning(language, message: str, ip_address: str):
    if message.lower() == "yes":
      return CovidScreaning.generate_screaning_results(language, ip_address)  # show screaning results
    elif message.lower() == "no":
      return CovidScreaning.restartscreaning(language, ip_address)
    else:
      return language.VIEW_OR_RESTART_MESSAGE