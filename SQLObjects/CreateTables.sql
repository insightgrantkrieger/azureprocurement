/****** Object:  Table [dbo].[Prompt]    Script Date: 18/06/2024 1:07:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Prompt](
	[PromptID] [bigint] IDENTITY(1,1) NOT NULL,
	[PromptGroupID] [bigint] NOT NULL,
	[Description] [nvarchar](500) NOT NULL,
	[UserPrompt] [nvarchar](max) NOT NULL,
	[SystemPrompt] [nvarchar](max) NOT NULL,
	[AISearchText] [nvarchar](max) NOT NULL,
	[IsActive] [bit] NOT NULL,
 CONSTRAINT [PK_Prompt] PRIMARY KEY CLUSTERED 
(
	[PromptID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PromptGroup]    Script Date: 18/06/2024 1:07:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PromptGroup](
	[PromptGroupID] [bigint] IDENTITY(1,1) NOT NULL,
	[PromptGroupName] [nvarchar](100) NULL,
 CONSTRAINT [PK_PromptGroup] PRIMARY KEY CLUSTERED 
(
	[PromptGroupID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PromptOutput]    Script Date: 18/06/2024 1:07:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PromptOutput](
	[PromptOutputID] [bigint] IDENTITY(1,1) NOT NULL,
	[PromptID] [bigint] NOT NULL,
	[ResponseID] [bigint] NOT NULL,
	[PromptOutput] [nvarchar](max) NULL,
	[PromptScore] [int] NULL,
	[OutputDateTime] [datetime2](7) NOT NULL,
 CONSTRAINT [PK_PromptOutput] PRIMARY KEY CLUSTERED 
(
	[PromptOutputID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PromptOutputRaw]    Script Date: 18/06/2024 1:07:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/****** Object:  Table [dbo].[Response]    Script Date: 18/06/2024 1:07:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Response](
	[ResponseID] [bigint] IDENTITY(1,1) NOT NULL,
	[ResponseDesc] [nvarchar](150) NULL,
 CONSTRAINT [PK_Student] PRIMARY KEY CLUSTERED 
(
	[ResponseID] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Prompt] ADD  CONSTRAINT [DF__Prompt__IsActive__1BC821DD]  DEFAULT ((1)) FOR [IsActive]
GO
ALTER TABLE [dbo].[PromptOutput] ADD  CONSTRAINT [DF_PromptOutput_OutputDateTime]  DEFAULT (getdate()) FOR [OutputDateTime]
GO
ALTER TABLE [dbo].[PromptOutput]  WITH CHECK ADD  CONSTRAINT [FK_PromptOutput_Response] FOREIGN KEY([ResponseID])
REFERENCES [dbo].[Response] ([ResponseID])
GO
ALTER TABLE [dbo].[PromptOutput] CHECK CONSTRAINT [FK_PromptOutput_Response]
GO
ALTER TABLE [dbo].[PromptOutputRaw]  WITH CHECK ADD  CONSTRAINT [FK_PromptOutputRaw_Prompt] FOREIGN KEY([PromptID])
REFERENCES [dbo].[Prompt] ([PromptID])
GO
ALTER TABLE [dbo].[PromptOutputRaw] CHECK CONSTRAINT [FK_PromptOutputRaw_Prompt]
GO
