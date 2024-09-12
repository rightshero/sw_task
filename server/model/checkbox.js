const { Sequelize, DataTypes } = require("sequelize");
const db = require("../utils/database");

const Checkbox = db.define("Checkbox", {
  level: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    allowNull: false,
  },
  choice: {
    type: DataTypes.STRING,
    allowNull: false,
    validate: {
      is: /^[A|B]$/,
    },
  },
});

module.exports = Checkbox;
