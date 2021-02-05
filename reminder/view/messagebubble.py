CAROUSEL = {
    "type": "carousel",
    "contents": []
}


SCHEDULE_BUBBLE = {
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "time",
        "align": "start",
        "margin": "xs",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "style": "normal",
        "decoration": "none",
        "offsetTop": "none",
        "offsetBottom": "none",
        "offsetStart": "xxl",
        "color": "#ffffff"
      }
    ],
    "backgroundColor": "#2f4f4f"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "name",
        "size": "xl",
        "wrap": True
      },
      {
        "type": "text",
        "text": "message",
        "wrap": True
      }
    ],
    "backgroundColor": "#ddffee"
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
        "style": "secondary",
        "color": "#77bb88"
      }
    ],
    "backgroundColor": "#ddffee"
  },
  "styles": {
    "header": {
      "backgroundColor": "#88ff88",
      "separator": False,
      "separatorColor": "#00ff00"
    }
  }
}