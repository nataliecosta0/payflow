import 'package:flutter/material.dart';
import 'package:payflow/shared/themes/app_colors.dart';
import 'package:payflow/shared/widgets/divider_vertical/divider_vertical_widget.dart';
import 'package:payflow/shared/widgets/social_login/label_button/label_button.dart';

class SetLabelButtons extends StatelessWidget {
  final String labelPrimary;
  final VoidCallback onTapPrimary;
  final String labelSecondary;
  final VoidCallback onTapSecondary;
  final bool enablePrimaryColor;
  const SetLabelButtons({
    Key? key,
    required this.labelPrimary,
    required this.onTapPrimary,
    required this.labelSecondary,
    required this.onTapSecondary,
    this.enablePrimaryColor = false,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
        color: AppColors.background,
        height: 56,
        child: Row(
          children: [
            if (enablePrimaryColor) ...[
              LabelButton.primary(
                label: labelPrimary,
                onPressed: onTapPrimary,
              ),
            ] else ...[
              LabelButton.heading(
                label: labelPrimary,
                onPressed: onTapPrimary,
              ),
            ],
            DividerVerticalWidget(
              height: 56,
            ),
            LabelButton.heading(
              label: labelSecondary,
              onPressed: onTapSecondary,
            )
          ],
        ));
  }
}