const path = require("path");

module.exports = {
  publicPath: process.env.VUE_APP_STATIC_URL,
  outputDir: path.resolve(__dirname, "../devops_logbook/static"),
  indexPath: path.resolve(__dirname, "../devops_logbook/templates/", "index.html"),
  runtimeCompiler: true,
};
