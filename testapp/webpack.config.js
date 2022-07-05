var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');


module.exports = {
  entry:  path.join(__dirname, './frontend/src/index'),
  output: {
    path: path.join(__dirname, 'assets/dist'),
    filename: '[name].js'
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
  ],
  module: {
    rules: [
      {
        test: /\.js|.jsx$/,
        exclude: [
          path.resolve(__dirname, '/node_modules/'),
          path.resolve(__dirname, '/frontend/node_modules/')
        ],
        use: "babel-loader",
      },
      {
        test: /\.css$/,
        exclude: [
          path.resolve(__dirname, '/node_modules/'),
          path.resolve(__dirname, '/frontend/node_modules/')
        ],
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
}
