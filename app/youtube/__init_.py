from flask import Blueprint , request , jsinofy

youtube_bp = blueprint(
  " youtube ",
  __name__
  )

@youtube_bp.route(
  "/play" ,
  methods =["POST"]
)
def play ():

  data = request.get_json(
    silent = True
    )or {}

command = data.get(
"command",
 ""
).strip()

if not command :
  return jsonify({
    "success":"false",
    "message":"there is no song name, mentioned"}
  )400
