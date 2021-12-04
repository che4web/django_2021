const webpack = require('webpack')
module.exports = {

  "publicPath": "/",
  "assetsDir": "static",
  "indexPath": "templates/index.html",
configureWebpack: {
    plugins: [
      new webpack.IgnorePlugin({
        resourceRegExp: /^\.\/locale$/,
        contextRegExp: /moment$/
      })
    ]
},
  "filenameHashing": true,

  "devServer": {
    "proxy": {
      "^/api": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/admin": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/media": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
      "^/static": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      },
        "^/accounts/login": {
        "target": "http://localhost:8000",
        "ws": true,
        "changeOrigin": true
      }
    }
  },

  "transpileDependencies": [
  ],

  productionSourceMap: false,

}
