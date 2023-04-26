# The **M**odel **V**iew **C**ontroller pattern

# Table of contents

1. [Definition](#definition)
2. [Model](#model)
3. [View](#view)
4. [Controller](#controller)
5. [Workflow](#workflow)
6. [References](#references)

## 1. Definition <a name="definition"></a>

The `Model-View-Controller` (MVC) is an **architectural pattern** that separates an application into three main logical components: `the model`, `the view`, and `the controller`. Each of these components are built to handle specific development aspects of an application.

## 2. Model <a name="model"></a>

The `Model` component corresponds to all the data-related logic that the user works with. This can represent either the data that is being transferred between the View and Controller components or any other business logic-related data. For example, a Customer object will retrieve the customer information from the database, manipulate it and update it data back to the database or use it to render data.

## 3. View <a name="view"></a>

The `View` component is used for all the UI logic of the application. For example, the Customer view will include all the UI components such as text boxes, dropdowns, etc. that the final user interacts with.

## 4. Controller <a name="controller"></a>

`Controllers` act as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model component and interact with the Views to render the final output. For example, the Customer controller will handle all the interactions and inputs from the Customer View and update the database using the Customer Model. The same controller will be used to view the Customer data.

## 5. Workflow <a name="workflow"></a>

This is an example of an MVC web application workflow.

- The client browser sends `request` to the MVC Application.

- The web application receives this request and performs `routing` based on the URL of the incoming `request`.

- This routing operation calls the `appropriate controller` and executes it.

- `The Controller` processes the data using `Model` and invokes the appropriate method.

- The processed `Model` is then passed to the `View`, which in turn `renders the final output`.

## 6. References <a name="references"></a>

This document was created with the help of [tutorialspoint.com article about MVC](https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm).
