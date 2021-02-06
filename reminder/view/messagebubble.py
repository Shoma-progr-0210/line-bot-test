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
    "backgroundColor": "#2f4f4f",
    "cornerRadius": "none",
    "borderWidth": "none"
  },
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://.png",
        "size": "0%"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "backgroundColor": "#00C7C7"
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
        "margin": "lg",
        "wrap": True
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
        "color": "#007878"
      }
    ],
    "backgroundColor": "#ffffff"
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
    "backgroundColor": "#182047",
    "cornerRadius": "none",
    "borderWidth": "none"
  },
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        "size": "0%"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "backgroundColor": "#1E799E"
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
        "margin": "lg",
        "wrap": True
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