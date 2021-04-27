module.exports = {
  transpileDependencies: ["vuetify"],

  pluginOptions: {
    i18n: {
      locale: "en",
      fallbackLocale: "en",
      localeDir: "locales",
      enableInSFC: true
    }
  },
  devServer: {
    watchOptions: {
      poll: true
    },
    proxy: {
      "": {
        target: "http://backend:82/",
        changeOrigin: true,
        ws: true
      }
    }
  }
};
console.log('111111');
