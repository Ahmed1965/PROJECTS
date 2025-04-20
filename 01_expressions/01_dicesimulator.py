{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP4OYRT38T/QXKBrU/6FBrH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ahmed1965/PROJECTS/blob/main/01_expressions/01_dicesimulator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "bv141gp4eVJW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ba488447-0a17-4b3a-8775-d82a7f59b16c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter First Number: 2\n",
            "Enter Second Number: 4\n",
            "The sum of 2 and 4 is:  6\n"
          ]
        }
      ],
      "source": [
        "def add_two_numbers():\n",
        "  number1 = int(input(\"Enter First Number: \"))\n",
        "  number2 = int(input(\"Enter Second Number: \"))\n",
        "  sum = number1 + number2\n",
        "  print(f\"The sum of {number1} and {number2} is:  {sum}\")\n",
        "add_two_numbers()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 02_agreement_bot\n",
        "# Problem Statement\n",
        "Write a program which asks the user what their favorite animal is, and then always responds with \"My favorite animal is also ___!\" (the blank should be filled in with the user-inputted animal, of course)."
      ],
      "metadata": {
        "id": "Ud4Vx2Y-TM4s"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def favorite_animal():\n",
        "  animal = input(\"Enter your favourite animal:  \")\n",
        "  print(f\"My favourite animal is also {animal}\")\n",
        "favorite_animal()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KAAq2ZUhTSaS",
        "outputId": "8cc49169-7db7-46a6-ed42-7b25e381a559"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your favourite animal:  Elephant\n",
            "My favourite animal is also Elephant\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 03_fahrenheit_to_celsius\n",
        "# Problem Statement\n",
        "Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius."
      ],
      "metadata": {
        "id": "zbWF7SRTUh1w"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def convert_into_celsius():\n",
        "  fahrenheit = float(input(\"Enter temperature in Fahrenheit:  \"))\n",
        "  celsius = (fahrenheit - 32) * 5/9\n",
        "  print(f\"{fahrenheit} Fahrenheit is equal to {celsius}\\u00B0C Celsius\")\n",
        "convert_into_celsius()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e7bhaqjHVBX2",
        "outputId": "bfae6d52-fb0e-46aa-b53b-69210f73b316"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter temperature in Fahrenheit:  76\n",
            "76.0 Fahrenheit is equal to 24.444444444444443°C Celsius\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 04_how_old_are_they\n",
        "# Problem Statement\n",
        "Write a program to solve this age-related riddle!\n",
        "\n",
        "Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:\n",
        "\n",
        "Anton is 21 years old.\n",
        "Beth is 6 years older than Anton.\n",
        "Chen is 20 years older than Beth.\n",
        "Drew is as old as Chen's age plus Anton's age.\n",
        "Ethan is the same age as Chen.\n",
        "\n",
        "Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):\n",
        "\n",
        "Anton is 3\n",
        "\n",
        "Beth is 4\n",
        "\n",
        "Chen is 5\n",
        "\n",
        "Drew is 6\n",
        "\n",
        "Ethan is 7"
      ],
      "metadata": {
        "id": "A1kA0D5vWgni"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def age_riddle():\n",
        "  anton = 21\n",
        "  beth = 21+6\n",
        "  chen = beth+20\n",
        "  drew = chen + anton\n",
        "  ethan = chen\n",
        "  print(f\"The age of Anton is {anton}\")\n",
        "  print(f\"The age of Beth is {beth}\")\n",
        "  print(f\"The age of Chen is {chen}\")\n",
        "  print(f\"The age of Drew is {drew}\")\n",
        "  print(f\"The age of Ethan is {ethan}\")\n",
        "age_riddle()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z9wD70bzW7QF",
        "outputId": "3c16f07b-1689-4306-9750-7f2b6a4cfbd8"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The age of Anton is 21\n",
            "The age of Beth is 27\n",
            "The age of Chen is 47\n",
            "The age of Drew is 68\n",
            "The age of Ethan is 47\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 05_triangle_perimeter\n",
        "# Problem Statement\n",
        "Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).\n",
        "\n",
        "Here's a sample run of the program (user input is in bold italics):\n",
        "\n",
        "What is the length of side 1? 3\n",
        "\n",
        "What is the length of side 2? 4\n",
        "\n",
        "What is the length of side 3? 5.5\n",
        "\n",
        "The perimeter of the triangle is 12.5"
      ],
      "metadata": {
        "id": "P070eY8kZpFV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.display import display, HTML\n",
        "def triangle_side_sum():\n",
        "  side_1 = float(input(\"Enter the length of side 1:  \"))\n",
        "  display(HTML(f\"<i><b>{side_1}</b></i>\"))\n",
        "  side_2 = float(input(\"Enter the length of side 2:  \"))\n",
        "  display(HTML(f\"<i><b>{side_2}</b></i>\"))\n",
        "  side_3 = float(input(\"Enter the length of side 3:  \"))\n",
        "  display(HTML(f\"<i><b>{side_3}</b></i>\"))\n",
        "  perimeter = side_1 + side_2 + side_3\n",
        "  print(f\"The perimeter of the triangle is {perimeter}\")\n",
        "\n",
        "triangle_side_sum()"
      ],
      "metadata": {
        "id": "87TunN-saEwO",
        "outputId": "806fa7aa-af35-435e-ea95-67043e0ad356",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 138
        }
      },
      "execution_count": 18,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter the length of side 1:  3\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<i><b>3.0</b></i>"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter the length of side 2:  4\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<i><b>4.0</b></i>"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter the length of side 3:  5.5\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<i><b>5.5</b></i>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The perimeter of the triangle is 12.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 06_square_number\n",
        "# Problem Statement\n",
        "Ask the user for a number and print its square (the product of the number times itself).\n",
        "\n",
        "Here's a sample run of the program (user input is in bold italics):\n",
        "\n",
        "Type a number to see its square: 4\n",
        "\n",
        "4.0 squared is 16.0"
      ],
      "metadata": {
        "id": "Z-8fAiH5b3ej"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def square_of_a_number():\n",
        "  square_number = float(input(\"Enter a number to see its square: \"))\n",
        "  display(HTML(f\"<i><b>{square_number}</b></i>\"))\n",
        "  square = square_number * square_number\n",
        "  print(f\"{square_number} squared is {square}\")\n",
        "square_of_a_number()"
      ],
      "metadata": {
        "id": "u66hkTkFcJje",
        "outputId": "bf90714a-1d33-40a7-b58f-4851df295017",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        }
      },
      "execution_count": 19,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter a number to see its square: 6\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<i><b>6.0</b></i>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6.0 squared is 36.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# PROJECTS/homework_projects/01_expressions/01_dicesimulator.md\n",
        "\n",
        "# Problem Statement\n",
        "Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.\n"
      ],
      "metadata": {
        "id": "N5JVKw2mksRq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def dice_roll():\n",
        "\n",
        "  diceRoll_1 = random.randint(1,6)\n",
        "  diceRoll_2 = random.randint(1,6)\n",
        "  return diceRoll_1, diceRoll_2\n",
        "def simulateDice():\n",
        "  for _ in range(3):\n",
        "    diceRoll_1, diceRoll_2 = dice_roll()\n",
        "    print(f\"Die 1 : {diceRoll_1} Die 2 : {diceRoll_2}\")\n",
        "\n",
        "simulateDice()\n"
      ],
      "metadata": {
        "id": "0wor817Mk-Nr",
        "outputId": "ce5fb65f-fa5f-4287-e2d5-8d2b4bd98809",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Die 1 : 5 Die 2 : 5\n",
            "Die 1 : 1 Die 2 : 4\n",
            "Die 1 : 4 Die 2 : 1\n"
          ]
        }
      ]
    }
  ]
}