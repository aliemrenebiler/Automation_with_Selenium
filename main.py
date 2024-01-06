"Main"


from workflows.product_content_workflows import ProductContentWorkflows


def main():
    "Main Function"

    pc_workflows = ProductContentWorkflows()

    pc_workflows.compare_product_information()


if __name__ == "__main__":
    main()
