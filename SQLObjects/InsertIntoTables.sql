SET IDENTITY_INSERT [dbo].[Prompt] ON 
GO
INSERT [dbo].[Prompt] ([PromptID], [PromptGroupID], [Description], [UserPrompt], [SystemPrompt], [AISearchText], [IsActive]) VALUES (1, 1, N'Insurance Check', N'Does the supplier meet the insurance requirements of having insurance for the required period?', N'You are an insurance bot', N'Insurance Check', 1)
GO
INSERT [dbo].[Prompt] ([PromptID], [PromptGroupID], [Description], [UserPrompt], [SystemPrompt], [AISearchText], [IsActive]) VALUES (2, 1, N'Training pricing check', N'Rate the Respondents Pricing to undertake Training
.', N'You are a trainign assessor bot', N'Training costs', 1)
GO
INSERT [dbo].[Prompt] ([PromptID], [PromptGroupID], [Description], [UserPrompt], [SystemPrompt], [AISearchText], [IsActive]) VALUES (3, 1, N'Experience', N'Rate the Respondents / Facilitators Qualifications and Experience.
', N'General bot', N'experience', 1)
GO
SET IDENTITY_INSERT [dbo].[Prompt] OFF
GO
SET IDENTITY_INSERT [dbo].[PromptGroup] ON 
GO
INSERT [dbo].[PromptGroup] ([PromptGroupID], [PromptGroupName]) VALUES (1, N'General')
GO
SET IDENTITY_INSERT [dbo].[PromptGroup] OFF
GO
SET IDENTITY_INSERT [dbo].[Response] ON 
GO
INSERT [dbo].[Response] ([ResponseID], [ResponseDesc]) VALUES (1, N'Company 1')
GO
SET IDENTITY_INSERT [dbo].[Response] OFF
GO
