const express = require("express");
const router = express.Router();
const checkboxController = require("../controller/checkboxController");

router.get("/", checkboxController.getCheckboxes);
router.post("/", checkboxController.postCheckbox);
router.delete("/", checkboxController.deleteCheckbox);
router.put("/", checkboxController.putCheckbox);

module.exports = router;
