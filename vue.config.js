module.exports = {
  devServer: {
    host: 'sdg-courses.wpi.edu'
  },	
    publicPath: process.env.NODE_ENV === 'production'
        ? '/'
        : '/'
}
