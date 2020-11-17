function main(splash, args)
  --[[headers = {
    ['User-Agent'] = "watson"
  }
  splash:set_custom_headers(headers)]]--
  splash:on_request(function(request)
    request:set_header("User-Agent", "watson")
    end)
  --splash:set_user_agent("alou")
  assert(splash:go(args.url))
  assert(splash:wait(1))
  input_box = assert(splash:select("#search_form_input_homepage"))
  input_box:focus()
  input_box:send_text("my user agent")
  assert(splash:wait(0.5))
  --[[
  btn = assert(splash:select("#search_button_homepage"))
  btn:mouse_click()
  ]]--
  input_box:send_keys("<Enter>")
  assert(splash:wait(3))
  splash:set_viewport_full()
  return {
    html = splash:html(),
    png = splash:png(),
  }
end