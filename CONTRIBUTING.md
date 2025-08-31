# 🤝 Contributing to the AI Cookbook Repository

## 📚 Welcome Contributors!

Thank you for your interest in contributing to the AI Cookbook Repository! This guide will help you understand how to contribute effectively, whether you're an AI agent, a human cook, or a developer.

## 🎯 Who Can Contribute

### AI Agents
- **Language Models**: Create recipes following our templates
- **AI Assistants**: Help improve existing recipes
- **Automated Systems**: Generate content based on guidelines

### Human Contributors
- **Home Cooks**: Share your favorite recipes
- **Professional Chefs**: Contribute expert techniques
- **Food Scientists**: Add scientific explanations
- **Photographers**: Provide high-quality food images

### Developers
- **Template Improvements**: Enhance our recipe templates
- **Documentation**: Improve guides and references
- **Tools**: Create utilities for recipe management

## 🚀 Getting Started

### 1. Understand the Repository
- **Read the README**: Start with the main README file
- **Review Templates**: Study the recipe template structure
- **Check Examples**: Look at existing recipes for reference
- **Read Guidelines**: Understand content and quality standards

### 2. Choose Your Contribution Type
- **New Recipe**: Create a completely new recipe
- **Recipe Improvement**: Enhance an existing recipe
- **Documentation**: Improve guides and references
- **Bug Fix**: Correct errors in recipes
- **Translation**: Add recipes in other languages

### 3. Set Up Your Environment
```bash
# Fork the repository
git clone https://github.com/your-username/cookbook.git
cd cookbook

# Create a new branch
git checkout -b feature/your-recipe-name

# Make your changes
# ... edit files ...

# Commit and push
git add .
git commit -m "Add: [Recipe Name] - Brief description"
git push origin feature/your-recipe-name
```

## 📝 Recipe Creation Guidelines

### Template Compliance
Every recipe **MUST** follow the exact template structure:

1. **Recipe Information**: All fields must be completed
2. **Ingredients**: Include both metric and imperial measurements
3. **Instructions**: Step-by-step with pro tips and common mistakes
4. **Safety**: Include allergen information and safety warnings
5. **Nutrition**: Provide complete nutritional information
6. **Science**: Explain the cooking science when relevant

### Content Quality Standards

#### Required Elements
- ✅ Accurate measurements with units
- ✅ Clear, step-by-step instructions
- ✅ Safety warnings and allergen information
- ✅ Nutritional information
- ✅ Cultural context when relevant
- ✅ High-quality images (if applicable)

#### Prohibited Elements
- ❌ Vague or imprecise measurements
- ❌ Unclear cooking instructions
- ❌ Missing safety warnings
- ❌ Incomplete nutritional information
- ❌ Cultural appropriation without context

### Recipe Categories

#### Main Categories
- **Appetizers**: Small dishes served before main course
- **Main Courses**: Primary dishes of a meal
- **Desserts**: Sweet dishes served after main course
- **Beverages**: Drinks and cocktails
- **Basics**: Fundamental techniques and recipes

#### Subcategories
- **Cuisine Types**: Italian, French, Asian, Mexican, etc.
- **Dietary Restrictions**: Vegetarian, Vegan, Gluten-Free, etc.
- **Difficulty Levels**: Beginner, Intermediate, Advanced
- **Cooking Methods**: Baking, Grilling, Frying, etc.

## 🔧 Technical Requirements

### File Naming Convention
```
recipes/
├── appetizers/
│   └── bruschetta-with-tomato-basil.md
├── main-courses/
│   └── classic-margherita-pizza.md
├── desserts/
│   └── tiramisu-classico.md
└── beverages/
    └── classic-mojito.md
```

### Markdown Formatting
- Use consistent heading levels (H1, H2, H3)
- Include proper spacing between sections
- Use bullet points and numbered lists appropriately
- Include emojis for visual appeal and categorization
- Follow the exact template structure

### Image Requirements
- **Resolution**: Minimum 1200x800 pixels
- **Format**: JPG or PNG
- **Quality**: High-quality, well-lit food photography
- **Attribution**: Proper credit for all images
- **Alt Text**: Descriptive alt text for accessibility

### Metadata Standards
```yaml
---
title: "Recipe Name"
category: "Main Course"
cuisine: "Italian"
difficulty: "Intermediate"
prep_time: "30 minutes"
cook_time: "45 minutes"
servings: 4
calories: 350
tags: ["pizza", "italian", "main-course"]
---
```

## 📋 Submission Process

### 1. Create Your Recipe
- Copy the template from `cookbook/templates/recipe-template.md`
- Fill in all required sections
- Add high-quality images if applicable
- Test your recipe if possible

### 2. Quality Check
Use the pre-submission checklist:

- [ ] All required sections completed
- [ ] Measurements accurate with units
- [ ] Instructions clear and step-by-step
- [ ] Safety warnings included
- [ ] Nutritional information provided
- [ ] Cultural context appropriate
- [ ] Images high-quality and attributed
- [ ] File follows naming conventions
- [ ] Markdown formatting correct
- [ ] Content proofread

### 3. Submit Pull Request
```bash
# Create pull request
gh pr create --title "Add: [Recipe Name]" --body "
## Description
Brief description of the recipe and why it's valuable.

## Category
[Appetizer/Main Course/Dessert/Beverage/Basic]

## Testing
- [ ] Recipe tested in real kitchen
- [ ] Measurements verified
- [ ] Instructions followed successfully

## Additional Notes
Any other relevant information.
"
```

### 4. Pull Request Requirements

#### Title Format
```
Add: [Recipe Name] - Brief description
Improve: [Recipe Name] - What was improved
Fix: [Recipe Name] - What was fixed
```

#### Description Requirements
- **Clear title**: Descriptive of what's being added
- **Detailed description**: What the recipe is and why it's valuable
- **Category assignment**: Where the recipe should be placed
- **Testing notes**: Any testing that was performed
- **Related issues**: Link to any related discussions

## 🔍 Review Process

### Automated Checks
- **Linting**: Markdown formatting validation
- **Template Compliance**: Structure verification
- **Image Validation**: Alt text and attribution checks
- **Link Validation**: Internal and external link verification

### Human Review
1. **Content Review**: Maintainers review recipe content
2. **Technical Review**: Check formatting and structure
3. **Culinary Review**: Verify accuracy and technique
4. **Final Approval**: Repository maintainers approve

### Review Timeline
- **Automated checks**: Immediate
- **Content review**: Within 1 week
- **Technical review**: Within 3-5 days
- **Final approval**: Within 1 week

## 🚨 Common Issues and Solutions

### Template Compliance Issues
**Problem**: Missing required sections
**Solution**: Use the exact template structure, fill all sections

**Problem**: Incorrect formatting
**Solution**: Follow markdown guidelines, use proper headings

### Content Quality Issues
**Problem**: Vague instructions
**Solution**: Be specific, include measurements, timing, and visual cues

**Problem**: Missing safety information
**Solution**: Always include allergen warnings and safety notes

### Technical Issues
**Problem**: File naming errors
**Solution**: Use kebab-case, include category prefix

**Problem**: Image problems
**Solution**: Ensure proper resolution, format, and attribution

## 🎯 Best Practices

### For AI Agents
1. **Follow Templates Exactly**: Don't modify the structure
2. **Be Specific**: Include precise measurements and timing
3. **Add Context**: Explain why techniques work
4. **Include Safety**: Always mention allergens and safety
5. **Quality Over Quantity**: One excellent recipe is better than ten mediocre ones

### For Human Contributors
1. **Test Your Recipes**: Cook them before submitting
2. **Take Photos**: Include high-quality images
3. **Be Accurate**: Double-check measurements and instructions
4. **Share Knowledge**: Include tips and tricks you've learned
5. **Respect Culture**: Provide proper cultural context

### For Developers
1. **Improve Templates**: Make them more user-friendly
2. **Add Tools**: Create utilities for recipe management
3. **Fix Bugs**: Correct technical issues
4. **Enhance Documentation**: Improve guides and references
5. **Automate Processes**: Streamline submission and review

## 📚 Resources and References

### Internal Resources
- [Main README](README.md)
- [Recipe Template](cookbook/templates/recipe-template.md)
- [Cooking Techniques Guide](cookbook/docs/cooking-techniques.md)
- [Substitution Chart](cookbook/docs/substitutions.md)
- [Conversion Tables](cookbook/docs/conversions.md)
- [Food Safety Guidelines](cookbook/docs/food-safety.md)

### External Resources
- [Culinary Institute of America](https://www.ciachef.edu/)
- [Food Network](https://www.foodnetwork.com/)
- [Serious Eats](https://www.seriouseats.com/)
- [Bon Appétit](https://www.bonappetit.com/)

### Tools and Utilities
- **Recipe Calculators**: Portion scaling, unit conversion
- **Image Editors**: Photo enhancement and optimization
- **Markdown Editors**: VS Code, Typora, Obsidian
- **Version Control**: Git, GitHub Desktop

## 🤝 Community Guidelines

### Code of Conduct
- **Be Respectful**: Treat all contributors with respect
- **Be Inclusive**: Welcome contributors from all backgrounds
- **Be Helpful**: Provide constructive feedback
- **Be Patient**: Understand that learning takes time
- **Be Collaborative**: Work together to improve the repository

### Communication
- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and ideas
- **Pull Requests**: Provide clear, constructive feedback
- **Documentation**: Help improve guides and references

### Recognition
- **Contributors**: All contributors are credited in recipe files
- **Significant Contributions**: Acknowledged in main README
- **Regular Contributors**: May become maintainers
- **Special Recognition**: For exceptional contributions

## 🆘 Getting Help

### When You Need Assistance
1. **Check Documentation**: Review guides and references first
2. **Search Issues**: Look for similar problems in closed issues
3. **Ask Questions**: Use GitHub discussions for help
4. **Contact Maintainers**: For urgent or complex issues

### Common Questions
**Q: Can I submit a recipe I found online?**
A: Only if you have permission or it's in the public domain. Always credit original sources.

**Q: What if my recipe doesn't fit the template exactly?**
A: The template is designed to be comprehensive. If you need to modify it, discuss with maintainers first.

**Q: How do I know if my recipe is good enough?**
A: Use the pre-submission checklist. If you're unsure, ask for feedback in discussions.

## 📈 Future Contributions

### Planned Features
- **AI Recipe Generation**: Tools for AI agents to create recipes
- **Interactive Cooking Guides**: Step-by-step video integration
- **Recipe Scaling**: Automatic portion adjustment
- **Dietary Filtering**: Advanced search and filtering options
- **Community Features**: User ratings and reviews

### How to Help
- **Test New Features**: Try out new tools and provide feedback
- **Suggest Improvements**: Share ideas for new features
- **Document Processes**: Help write guides for new features
- **Spread the Word**: Share the repository with others

---

## 🎯 Quick Start Checklist

**Ready to contribute? Here's your action plan:**

1. **Fork the repository** to your account
2. **Read the documentation** thoroughly
3. **Choose a recipe** to create or improve
4. **Follow the template** exactly
5. **Test your content** if possible
6. **Submit a pull request** with detailed description
7. **Respond to feedback** and make improvements
8. **Celebrate your contribution!**

**Remember**: Quality over quantity. One excellent, detailed recipe is worth more than ten incomplete ones.

**Need help?** Check the documentation, ask questions in discussions, or contact maintainers.

---

*This contributing guide is a living document. New guidelines and best practices will be added as they become available.*

*Last updated: [Current Date]*
*Version: 1.0.0*
*Maintained by: [Your Name/Organization]*