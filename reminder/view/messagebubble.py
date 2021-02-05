CAROUSEL = {
    "type": "carousel",
    "contents": []
}


REMIND_BUBBLE = {
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
        "weight": "bold",
        "wrap": True
      },
      {
        "type": "text",
        "text": "message",
        "wrap": True
      }
    ],
    "backgroundColor": "#eeffee"
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
        "style": "secondary",
        "color": "#77bb88"
      }
    ],
    "backgroundColor": "#eeffee"
  },
  "styles": {
    "header": {
      "backgroundColor": "#88ff88",
      "separator": False,
      "separatorColor": "#00ff00"
    }
  }
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
    "backgroundColor": "#2f2f4f"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "name",
        "size": "xl",
        "weight": "bold",
        "wrap": True
      },
      {
        "type": "text",
        "text": "message",
        "wrap": True
      }
    ],
    "backgroundColor": "#ddddee"
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
        "color": "#6688cc"
      }
    ],
    "backgroundColor": "#ddddee"
  },
  "size": "kilo",
  "styles": {
    "header": {
      "backgroundColor": "#88ff88",
      "separator": False,
      "separatorColor": "#00ff00"
    }
  }
}