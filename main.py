"Main"


from workflows.compare_omniens_product_infos_with_ty_and_hb import (
    compare_omniens_product_infos_with_ty_and_hb,
)
from workflows.save_hepsiburada_merchant_product_urls_to_excel import (
    save_hepsiburada_merchant_product_urls_to_excel,
)
from workflows.save_trendyol_partner_product_urls_to_excel import (
    save_trendyol_partner_product_urls_to_excel,
)


def main():
    "Main Function"

    print()
    print("=== E-Marketing Management System (EMMA) ===\n")

    print("Product Content:")
    print("[1] Save Trendyol Partner Product URLs To Excel")
    print("[2] Save Hepsiburada Merchant Product URLs To Excel\n")
    print("[3] Compare Omniens Product Informations With Trendyol And Hepsiburada")

    selection = int(input("Selection: "))
    print()

    if selection == 1:
        save_trendyol_partner_product_urls_to_excel()
    elif selection == 2:
        save_hepsiburada_merchant_product_urls_to_excel()
    if selection == 3:
        compare_omniens_product_infos_with_ty_and_hb()
    else:
        print("(!) Invalid selection.")


if __name__ == "__main__":
    main()
