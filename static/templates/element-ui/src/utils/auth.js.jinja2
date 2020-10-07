const TokenKey = 'home_token'

export function getToken() {
  let token = localStorage.getItem(TokenKey)
  if (!token) {
    return null
  }
  let data = base2obj(token)
  if (data.exp * 1000 > new Date().valueOf()) {
    return token
  } else {
    localStorage.removeItem(TokenKey)
    return null
  }
}

export function setToken(token) {
  localStorage.setItem(TokenKey, token)
}

export function removeToken() {
  localStorage.removeItem(TokenKey)
}

export function base2obj(str) {
  let baseStr = str.split('.')[1]
  if (!baseStr) {
    return {}
  }
  return JSON.parse(window.atob(baseStr))
}

export const requests = []

export function cleanRequests() {
  while (requests.length) {
    requests.shift()()
  }
}
