const path = require('path')

module.exports = {
    entry: path.join(__dirname, 'src', 'index.js'),
    output: {
        path: path.resolve(__dirname, 'static', 'jobfindr'),
        filename: 'main.js'
    },
    module: {
        rules: [
            {
                test: /\.?jsx?$/,
                resolve: {
                    extensions: ['.js', '.jsx']
                },
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            }
        ]
    }
}