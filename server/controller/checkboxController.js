const Checkbox = require("../model/checkbox");
const { Op } = require("sequelize");

exports.getCheckboxes = async (req, res, next) => {
  try {
    const checkboxes = await Checkbox.findAll();
    res.status(200).json(checkboxes);
  } catch (error) {
    res.status(500).json({ error: "Failed to retrieve checkboxes" });
  }
};

exports.postCheckbox = async (req, res) => {
  try {
    const { level, choice } = req.body;
    const checkbox = await Checkbox.create({ level, choice });
    res.status(201).json(checkbox);
  } catch (error) {
    res.status(500).json({ error: "Failed to create checkbox" });
  }
};

exports.deleteCheckbox = async (req, res) => {
  try {
    const { level } = req.query;
    console.log(level);
    await Checkbox.destroy({
      where: { level: { [Op.gte]: level } },
    });
    res.status(200).json({ message: "Checkboxes removed" });
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Failed to delete checkboxes" });
  }
};

exports.putCheckbox = async (req, res) => {
  try {
    const { level, choice } = req.body;
    const [updated] = await Checkbox.update(
      { level, choice },
      { where: { level } }
    );
    if (updated) {
      const updatedCheckbox = await Checkbox.findByPk(level);
      await Checkbox.destroy({
        where: { level: { [Op.gt]: level } },
      });
      res.status(200).json(updatedCheckbox);
    } else {
      res.status(404).json({ message: "Checkbox not found" });
    }
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Failed to update checkbox" });
  }
};
