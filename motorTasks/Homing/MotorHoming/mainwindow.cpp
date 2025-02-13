#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <stdlib.h>
#include <iostream>
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QStringList motors;
    motors << "A" << "B" << "C" << "D" << "E";
    ui->comboBox->addItems(motors);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    std::string command = "python3.9 homing.py ";
    QString text = ui->comboBox->currentText();
    //std::cout<<text.toStdString();

    command += "motor" + text.toStdString() +".json";
    system(command.c_str());

}
