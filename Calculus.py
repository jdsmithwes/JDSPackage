{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Calculus.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNS6wRr4syDv4P6VfAmSk15",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/jdsmithwes/JDSPackage/blob/master/Calculus.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uGeGc0MlfUOj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def term_output(array, input_value):\n",
        "  \"\"\" This function evaluates a term at a specific x-value\n",
        "  Keywords\n",
        "  array: numpy array\n",
        "  input_value: value of x you are evaluating at\n",
        "\n",
        "  Return\n",
        "  Value of the term at designated input value\n",
        "    \"\"\"\n",
        "    return array[0]*(input_value**array[1])\n",
        "    pass\n",
        "\n",
        "def output_at(array_of_terms, x_value):\n",
        "\"\"\"When passed an array_of_terms and a value of  𝑥 , calculates the value of the function at that value.\n",
        "\n",
        "Keywords\n",
        "array_of_terms: numpy array that is the function being evaluated\n",
        "x_value: int - value of x you are evaluating entire function\n",
        "\n",
        "Return\n",
        "Value of the function at a designated input value     \"\"\"\n",
        "    outputs = []\n",
        "    for i in range(int(np.shape(array_of_terms)[0])):\n",
        "        outputs.append(array_of_terms[i][0]*x_value**array_of_terms[i][1])\n",
        "    return sum(outputs)\n",
        "    pass\n",
        "\n",
        "def delta_f(array_of_terms, x_value, delta_x):\n",
        "  \"\"\"When given a list_of_terms, an x_value, and a value  Δ𝑥 , returns the change in the output over that period.\n",
        "  \n",
        "  Keywords\n",
        "  array_of_terms: numpy array that is the function being evaluated\n",
        "  x_value: int - value of x you are evaluating the entire function\n",
        "  delta_x: int - movement along the x-axis    \"\"\"\n",
        "    return output_at(array_of_terms, x_value + delta_x) - output_at(array_of_terms, x_value)\n",
        "\n",
        "def derivative_of(array_of_terms, x_value, delta_x):\n",
        "  \"\"\" Finds the derivative of a function when given an x-value and delta x\n",
        "       \n",
        "       Keywords\n",
        "       array_of_terms: numpy array that is the function being evaluated\n",
        "       x_value: int - value of x you are evaluating the entire function\n",
        "       delta_x: int - movement along the x-axis  \"\"\"\n",
        "    return delta_f(array_of_terms,x_value,delta_x)/delta_x\n",
        "    pass"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}