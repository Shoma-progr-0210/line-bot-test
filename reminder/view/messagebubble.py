CAROUSEL = {
    "type": "carousel",
    "contents": []
}


REMIND_BUBBLE = {
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "2021/2/7 9:44",
            "size": "sm",
            "color": "#ffffff",
            "align": "center",
            "gravity": "center",
            "offsetTop": "none",
            "weight": "bold"
          }
        ],
        "backgroundColor": "#ffa500",
        "flex": 0,
        "position": "relative",
        "cornerRadius": "100px",
        "width": "200px",
        "height": "30px",
        "offsetEnd": "8px",
        "offsetBottom": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "name",
            "size": "xl",
            "weight": "bold",
            "wrap": True
          }
        ]
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "message",
        "margin": "none",
        "wrap": True,
        "offsetBottom": "lg"
      }
    ],
    "backgroundColor": "#ffffff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "確認",
          "data": "check"
        },
        "margin": "none",
        "style": "primary",
        "height": "sm",
        "color": "#d2691e"
      }
    ],
    "backgroundColor": "#ffffff"
  }
}

SCHEDULE_BUBBLE = {
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "time",
            "size": "sm",
            "color": "#ffffff",
            "align": "center",
            "gravity": "center",
            "offsetTop": "none",
            "weight": "bold"
          }
        ],
        "backgroundColor": "#66cdaa",
        "flex": 0,
        "position": "relative",
        "cornerRadius": "100px",
        "width": "200px",
        "height": "30px",
        "offsetEnd": "8px",
        "offsetBottom": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "name",
            "size": "xl",
            "weight": "bold",
            "wrap": True
          }
        ]
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "message",
        "margin": "none",
        "wrap": True,
        "offsetBottom": "lg"
      }
    ],
    "backgroundColor": "#ffffff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "編集",
          "data": "edit"
        },
        "margin": "none",
        "style": "primary",
        "height": "sm",
        "color": "#385077"
      }
    ],
    "backgroundColor": "#ffffff"
  }
}