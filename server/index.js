const express = require("express");
const cors = require("cors");
const app = express();
const bodyparser = require("body-parser");
const router = require("./routes/checkboxRoute");
const sequelize = require("./utils/database");
const checkbox = require("./model/checkbox");

app.use(bodyparser.json());
app.use(bodyparser.urlencoded({ extended: false }));

app.use(cors());

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
  next();
});

app.use(express.static("public"));
// app.use(express.json());
// app.use("/", router);

//test routes
app.get("/test", (req, res, next) => {
  res.send("hello world");
});

//CRUD routes
// app.use("/", require("./routes/checkboxRoute.js"));
// Sync Sequelize models with the database
// db.sequelize
//   .sync()
//   .then(() => {
//     console.log("Database synced");
//   })
//   .catch((error) => {
//     console.error("Error syncing database:", error);
//   });
app.use("/", router);
app.use("/clear", router);
// app.use("/:level", router);

app.use((error, req, res, next) => {
  console.log(error);
  const status = error.statusCode || 500;
  const message = error.message;
  res.status(status).json({ message: message });
});

sequelize
  .sync()
  .then((result) => {
    console.log("Database connected");
    // app.listen(5000, "0.0.0.0", () => {
    //   console.log("Server is running on port 5000");
    // });
    app.listen(5000);
  })
  .catch();

// const port = 5000;
// app.listen(port, () => {
//   console.log(`Server is listening on http://localhost:${port}`);
// });
