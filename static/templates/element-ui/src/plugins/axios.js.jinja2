'use strict'

import Vue from 'vue'
import axios from 'axios'
import { getToken, setToken, removeToken, requests } from '../utils/auth'

let config = {}

const service = axios.create(config)

service.interceptors.request.use(
  (config) => {
    // do something before request is sent
    if (config.method === 'get') {
      config.params = config.params || {}
      config.params._ = new Date().getTime()
    }

    const token = getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
      return config
    } else {
      window.postMessage(
        {
          cmd: 'getToken',
          params: {},
        },
        '*'
      )
      return new Promise((resolve) => {
        requests.push(() => {
          const token = getToken()
          config.headers.Authorization = `Bearer ${token}`
          resolve(config)
        })
      })
    }
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Add a response interceptor
service.interceptors.response.use(
  (response) => {
    if (response.config.responseType == 'blob') {
      return Promise.resolve(response)
    } else {
      let data = response.data
      if (data.code === 0) {
        return Promise.resolve(data)
        // return Promise.resolve(data)
      } else if ([101, 111, 112, 113].includes(data.code)) {
        // todo 没有token时暂存请求， 等待响应后调用
        window.postMessage(
          {
            cmd: 'getToken',
            params: {},
          },
          '*'
        )
        removeToken()
        return new Promise((resolve) => {
          requests.push(() => {
            const token = getToken()
            response.config.headers.Authorization = `Bearer ${token}`
            resolve(service(response.config))
          })
        })
      } else {
        console.log('data: ', data)
        return Promise.resolve(data)
      }
    }
  },
  (error) => {
    return Promise.reject(error)
  }
)

Plugin.install = function(Vue, options) {
  Vue.axios = service
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return service
      },
    },
    $axios: {
      get() {
        return service
      },
    },
  })
}

Vue.use(Plugin)

export default Plugin
