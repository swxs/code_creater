'use strict'

import Vue from 'vue'
import axios from 'axios'

const token =
  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTg1OTY2MjcsImlhdCI6MTU1ODU4OTQyNywiaXNzIjoiSURZOk1YIiwibmJmIjoxNTU4NTg5NDI3LCJvcmdfY29kZSI6ImlkeSIsIm9yZ19uYW1lIjoiXHU4MmNmXHU1ZGRlXHU0ZjE3XHU4YTAwXHU3ZjUxXHU3ZWRjXHU3OWQxXHU2MjgwXHU4MGExXHU0ZWZkXHU2NzA5XHU5NjUwXHU1MTZjXHU1M2Y4IiwidWlkIjoiNWNlMzZjZTZhNmM0OTBmY2UzMDA4MDc3IiwidW5hbWUiOiJcdThkODVcdTdlYTdcdTdiYTFcdTc0MDZcdTU0NTgiLCJhdmF0YXIiOm51bGwsInN1cGVyIjoxfQ.z6ikNmH8U3TB5XFNLtJxWo0l79_JnA-jctdabd6GsPE'
window.token = token

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let config = {
  // baseURL: process.env.baseURL || process.env.apiUrl || ""
  // timeout: 60 * 1000, // Timeout
  // withCredentials: true, // Check cross-site Access-Control
}

const _axios = axios.create(config)

_axios.interceptors.request.use(
  (config) => {
    // do something before request is sent
    const tem = config.url.indexOf('?') !== -1 ? '&' : '?'

    if (token) {
      config.headers = {
        Authorization: 'Bearer ' + token
      }
    }

    if (config.method === 'get') {
      config.url += tem + 'time_stamp=' + new Date().getTime()
    }

    return config
  },
  (error) => {
    console.log(error)
    return Promise.reject(error)
  }
)

// Add a response interceptor
_axios.interceptors.response.use(
  (data) => {
    if (data.data.code === 0) {
      return data.data.data
    } else {
      return Promise.reject(data.data.code)
    }
  },
  (error) => {
    console.log(error)
    return Promise.reject(error)
  }
)

Plugin.install = function(Vue, options) {
  Vue.axios = _axios
  window.axios = _axios
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios
      }
    },
    $axios: {
      get() {
        return _axios
      }
    }
  })
}

Vue.use(Plugin)

export default Plugin
